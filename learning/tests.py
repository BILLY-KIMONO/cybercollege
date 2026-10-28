from io import StringIO

from django.core.management import call_command
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Course, Enrollment, Lesson, LessonProgress


class LearningFlowTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="learner",
            password="A-strong-example-password-582!",
            email="learner@example.test",
        )
        self.course = Course.objects.create(
            title="Security Basics",
            slug="security-basics",
            category="Fundamentals",
            summary="Learn defensive basics.",
            description="A practical introduction.",
        )
        self.article = Lesson.objects.create(
            course=self.course,
            title="Start with the basics",
            lesson_type=Lesson.ARTICLE,
            content="Security is a team effort.",
        )
        self.lab = Lesson.objects.create(
            course=self.course,
            title="Respond to an alert",
            lesson_type=Lesson.LAB,
            content="A team member notices an unfamiliar sign-in.",
            challenge_prompt="What is the safest next step?",
            expected_answer="Report the sign-in through the approved security channel",
        )

    def test_registration_creates_and_signs_in_learner(self):
        response = self.client.post(
            reverse("register"),
            {
                "username": "new-learner",
                "email": "new@example.test",
                "password1": "A-different-strong-password-582!",
                "password2": "A-different-strong-password-582!",
            },
        )
        self.assertRedirects(response, reverse("dashboard"))
        self.assertTrue(User.objects.filter(username="new-learner").exists())
        self.assertIn("_auth_user_id", self.client.session)

    def test_course_enrollment_requires_sign_in_and_appears_in_dashboard(self):
        enroll_url = reverse("enroll", args=[self.course.slug])
        self.assertRedirects(
            self.client.post(enroll_url),
            f"{reverse('login')}?next={enroll_url}",
        )
        self.client.force_login(self.user)
        response = self.client.post(enroll_url)
        self.assertRedirects(response, self.course.get_absolute_url())
        self.assertTrue(Enrollment.objects.filter(user=self.user, course=self.course).exists())
        dashboard = self.client.get(reverse("dashboard"))
        self.assertContains(dashboard, self.course.title)

    def test_lesson_completion_requires_enrollment(self):
        self.client.force_login(self.user)
        response = self.client.post(
            reverse("complete_lesson", args=[self.course.slug, self.article.id])
        )
        self.assertRedirects(response, self.course.get_absolute_url())
        self.assertFalse(LessonProgress.objects.filter(user=self.user).exists())

    def test_lab_answer_is_checked_server_side_and_solution_is_not_rendered(self):
        self.client.force_login(self.user)
        Enrollment.objects.create(user=self.user, course=self.course)
        lesson_url = reverse("lesson_detail", args=[self.course.slug, self.lab.id])
        self.assertNotContains(
            self.client.get(lesson_url),
            self.lab.expected_answer,
        )

        completion_url = reverse("complete_lesson", args=[self.course.slug, self.lab.id])
        self.client.post(completion_url, {"answer": "Take an unsafe action"})
        self.assertFalse(
            LessonProgress.objects.filter(user=self.user, lesson=self.lab).exists()
        )

        self.client.post(
            completion_url,
            {"answer": "  REPORT THE SIGN-IN through the approved security channel  "},
        )
        self.assertTrue(
            LessonProgress.objects.filter(user=self.user, lesson=self.lab).exists()
        )

    def test_enrolled_course_without_lessons_has_working_detail_page(self):
        empty_course = Course.objects.create(
            title="Coming soon",
            slug="coming-soon",
            category="Fundamentals",
            summary="A future course.",
            description="Lessons are being prepared.",
        )
        self.client.force_login(self.user)
        Enrollment.objects.create(user=self.user, course=empty_course)
        response = self.client.get(empty_course.get_absolute_url())
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Lessons coming soon")


class DiplomaCurriculumTests(TestCase):
    def test_seed_demo_creates_all_modules_and_is_repeatable(self):
        call_command("seed_demo", stdout=StringIO())
        call_command("seed_demo", stdout=StringIO())

        modules = Course.objects.filter(semester__isnull=False).order_by(
            "semester", "module_code"
        )
        self.assertEqual(modules.count(), 24)
        self.assertEqual(set(modules.values_list("semester", flat=True)), {1, 2, 3, 4})
        self.assertEqual(
            set(modules.values_list("module_code", flat=True)),
            {f"CYB-{semester}{module:02d}" for semester in range(1, 5) for module in range(1, 7)},
        )
        self.assertEqual(Lesson.objects.filter(course__semester__isnull=False).count(), 192)
        for module in modules:
            lessons = module.lessons.all()
            self.assertEqual(module.duration, "40 hours", module.module_code)
            self.assertEqual(lessons.count(), 8, module.module_code)
            self.assertEqual(
                lessons.filter(lesson_type=Lesson.LAB).count(), 1, module.module_code
            )
            self.assertEqual(
                lessons.filter(lesson_type=Lesson.ARTICLE).count(), 7, module.module_code
            )
            total_hours = sum(
                int(lesson.duration.split()[0]) for lesson in lessons
            )
            self.assertEqual(total_hours, 40, module.module_code)
            lab = lessons.get(lesson_type=Lesson.LAB)
            self.assertTrue(lab.challenge_prompt, module.module_code)
            self.assertTrue(lab.expected_answer, module.module_code)
            self.assertLessEqual(len(lab.expected_answer), 160, module.module_code)
            self.assertNotIn(lab.expected_answer, lab.content, module.module_code)
            for lesson in lessons:
                self.assertGreaterEqual(
                    len(lesson.content.split()),
                    250,
                    f"{module.module_code}: {lesson.title}",
                )
                self.assertEqual(lesson.duration, "5 hours", module.module_code)
                for section in (
                    "LEARNING OUTCOMES",
                    "CORE LESSON NOTES",
                    "GUIDED PRACTICE",
                    "INDEPENDENT STUDY",
                    "KNOWLEDGE CHECK",
                    "ASSESSMENT AND REVIEW",
                    "Total: 300 minutes (5 hours).",
                ):
                    self.assertIn(
                        section, lesson.content, f"{module.module_code}: {lesson.title}"
                    )

    def test_catalog_lists_and_filters_diploma_modules(self):
        call_command("seed_demo", stdout=StringIO())

        response = self.client.get(reverse("catalog"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "24")
        self.assertContains(response, "four-semester")
        self.assertContains(response, "CYB-101")
        self.assertContains(response, "CYB-406")

        semester = self.client.get(reverse("catalog"), {"semester": "3"})
        self.assertEqual(semester.status_code, 200)
        self.assertContains(semester, "CYB-301")
        self.assertContains(semester, "CYB-306")
        self.assertNotContains(semester, "CYB-201")

        module = self.client.get(reverse("catalog"), {"q": "CYB-105"})
        self.assertContains(module, "Programming and Data Foundations for Cybersecurity")
        self.assertNotContains(module, "CYB-106")

    def test_diploma_module_detail_lists_lessons_and_safety_note(self):
        call_command("seed_demo", stdout=StringIO())
        module = Course.objects.get(module_code="CYB-402")

        response = self.client.get(module.get_absolute_url())

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "CYB-402")
        self.assertContains(response, "SEMESTER 4")
        self.assertContains(response, "Rules of engagement and safety")
        self.assertContains(response, "8 guided lessons")
        self.assertContains(response, "5 hours")
        self.assertEqual(len(response.context["course"].lessons.all()), 8)
