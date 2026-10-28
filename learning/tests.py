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
