from io import StringIO

from django.core.management import call_command
from django.contrib.auth.models import User
from django.test import TestCase
from django.urls import reverse

from .models import Course, Enrollment, Lesson, LessonProgress
from .professional_tracks import PROFESSIONAL_TRACKS


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

    def test_room_flow_shows_progress_navigation_and_resume_target(self):
        self.client.force_login(self.user)
        Enrollment.objects.create(user=self.user, course=self.course)

        course_page = self.client.get(self.course.get_absolute_url())
        self.assertContains(course_page, "ROOM 01")
        self.assertContains(course_page, "ROOM 02")
        self.assertContains(course_page, "Start this path")

        lesson_url = reverse("lesson_detail", args=[self.course.slug, self.article.id])
        lesson_page = self.client.get(lesson_url)
        self.assertContains(lesson_page, "ROOM 01")
        self.assertContains(lesson_page, "Next room")

        self.client.post(
            reverse("complete_lesson", args=[self.course.slug, self.article.id])
        )
        dashboard = self.client.get(reverse("dashboard"))
        self.assertContains(dashboard, "Next up: Respond to an alert")
        self.assertContains(
            dashboard,
            reverse("lesson_detail", args=[self.course.slug, self.lab.id]),
        )

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
        self.assertContains(response, "Rooms are being prepared")


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
                    450,
                    f"{module.module_code}: {lesson.title}",
                )
                self.assertEqual(lesson.duration, "5 hours", module.module_code)
                for section in (
                    "LEARNING OUTCOMES",
                    "CORE LESSON NOTES",
                    "DETAILED TEACHING NOTES",
                    "GUIDED PRACTICE",
                    "INDEPENDENT STUDY",
                    "KNOWLEDGE CHECK",
                    "MODEL ANSWER GUIDE",
                    "ASSESSMENT AND REVIEW",
                    "SUBMISSION CHECKLIST",
                    "Total: 300 minutes (5 hours).",
                ):
                    self.assertIn(
                        section, lesson.content, f"{module.module_code}: {lesson.title}"
                    )

    def test_threat_intelligence_lesson_teaches_its_core_lifecycle_and_analysis(self):
        call_command("seed_demo", stdout=StringIO())
        lessons = Lesson.objects.filter(course__module_code="CYB-401")
        lifecycle = lessons.get(title="Threat intelligence and confidence")
        sources = lessons.get(title="Malware defense and safe handling")
        dissemination = lessons.get(title="Sharing, privacy, and actionable reporting")

        for concept in (
            "collection",
            "analysis",
            "disseminate",
            "Strategic intelligence",
            "Operational intelligence",
            "Tactical intelligence",
            "indicator is a clue",
            "source reliability",
            "information credibility",
            "alternative explanations",
        ):
            self.assertIn(concept.casefold(), lifecycle.content.casefold())
        self.assertIn("approved reporting route", sources.content)
        self.assertIn("isolated environment", sources.content)
        self.assertIn("indicator alone does not establish", sources.content)
        self.assertIn("STIX", dissemination.content)
        self.assertIn("TAXII", dissemination.content)

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
        self.assertContains(response, "8 rooms")
        self.assertContains(response, "5 hours")
        self.assertEqual(len(response.context["course"].lessons.all()), 8)


class SpecialistCourseTests(TestCase):
    def test_seed_demo_creates_complete_specialist_courses(self):
        call_command("seed_demo", stdout=StringIO())
        call_command("seed_demo", stdout=StringIO())

        courses = Course.objects.filter(
            slug__in=[
                "practical-phishing-email-security",
                "secure-coding-essentials",
                "cloud-security-fundamentals",
            ]
        )
        self.assertEqual(courses.count(), 3)
        self.assertEqual(
            Lesson.objects.filter(course__in=courses).count(), 12
        )

        for course in courses:
            lessons = course.lessons.all()
            self.assertEqual(lessons.count(), 4, course.slug)
            self.assertEqual(course.duration, "4 hours", course.slug)
            self.assertIsNone(course.semester)
            self.assertEqual(
                lessons.filter(lesson_type=Lesson.LAB).count(), 1, course.slug
            )
            for lesson in lessons:
                self.assertEqual(lesson.duration, "1 hour", lesson.title)
                self.assertGreaterEqual(
                    len(lesson.content.split()), 150, lesson.title
                )
                for section in (
                    "LEARNING OUTCOMES",
                    "CORE LESSON NOTES",
                    "GUIDED PRACTICE",
                    "INDEPENDENT PRACTICE",
                    "KNOWLEDGE CHECK",
                    "ASSESSMENT AND REVIEW",
                    "Total: 60 minutes (1 hour).",
                ):
                    self.assertIn(section, lesson.content, lesson.title)

            lab = lessons.get(lesson_type=Lesson.LAB)
            self.assertTrue(lab.challenge_prompt, course.slug)
            self.assertTrue(lab.expected_answer, course.slug)
            self.assertNotIn(lab.expected_answer, lab.content, course.slug)

    def test_specialist_courses_are_searchable_in_catalog(self):
        call_command("seed_demo", stdout=StringIO())

        response = self.client.get(reverse("catalog"), {"q": "cloud security"})

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Cloud Security Fundamentals")
        self.assertNotContains(response, "Secure Coding Essentials")


class ProfessionalTrackTests(TestCase):
    def test_seed_demo_creates_complete_offensive_and_defensive_tracks(self):
        call_command("seed_demo", stdout=StringIO())
        call_command("seed_demo", stdout=StringIO())

        tracks = Course.objects.filter(
            slug__in=[
                "authorized-offensive-security-assessment",
                "defensive-security-operations-incident-response",
            ]
        )
        self.assertEqual(tracks.count(), 2)

        for track in tracks:
            lessons = track.lessons.all()
            self.assertEqual(track.duration, "40 hours", track.slug)
            self.assertEqual(lessons.count(), 8, track.slug)
            self.assertEqual(
                sum(int(lesson.duration.split()[0]) for lesson in lessons),
                40,
                track.slug,
            )
            self.assertEqual(
                lessons.filter(lesson_type=Lesson.LAB).count(), 1, track.slug
            )
            for lesson in lessons:
                self.assertEqual(lesson.duration, "5 hours", lesson.title)
                self.assertGreaterEqual(
                    len(lesson.content.split()), 250, lesson.title
                )
                for section in (
                    "LEARNING OUTCOMES",
                    "CORE LESSON NOTES",
                    "GUIDED PRACTICE",
                    "INDEPENDENT STUDY",
                    "KNOWLEDGE CHECK",
                    "ASSESSMENT AND REVIEW",
                    "Total: 300 minutes (5 hours).",
                ):
                    self.assertIn(section, lesson.content, lesson.title)

            lab = lessons.get(lesson_type=Lesson.LAB)
            self.assertTrue(lab.challenge_prompt, track.slug)
            self.assertTrue(lab.expected_answer, track.slug)
            self.assertLessEqual(len(lab.expected_answer), 160, track.slug)
            self.assertNotIn(lab.expected_answer, lab.content, track.slug)

        seeded_track_slugs = set(tracks.values_list("slug", flat=True))
        self.assertEqual(
            seeded_track_slugs,
            {track["slug"] for track in PROFESSIONAL_TRACKS},
        )

    def test_catalog_explains_both_professional_specializations(self):
        call_command("seed_demo", stdout=StringIO())

        response = self.client.get(reverse("catalog"))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "advanced defensive operations")
        self.assertContains(response, "authorized offensive assessment")
        self.assertContains(response, "Authorized Offensive Security Assessment")
        self.assertContains(
            response, "Defensive Security Operations and Incident Response"
        )
