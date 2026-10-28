from django.conf import settings
from django.db import models
from django.urls import reverse


class Course(models.Model):
    title = models.CharField(max_length=120)
    slug = models.SlugField(unique=True)
    category = models.CharField(max_length=60)
    summary = models.CharField(max_length=240)
    description = models.TextField()
    level = models.CharField(
        max_length=20,
        choices=[
            ("Beginner", "Beginner"),
            ("Intermediate", "Intermediate"),
            ("Advanced", "Advanced"),
        ],
        default="Beginner",
    )
    duration = models.CharField(max_length=40, default="2 hours")
    icon = models.CharField(max_length=12, default="◎")
    featured = models.BooleanField(default=False)
    published = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-featured", "title"]

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("course_detail", args=[self.slug])


class Lesson(models.Model):
    ARTICLE = "article"
    VIDEO = "video"
    LAB = "lab"
    LESSON_TYPES = [
        (ARTICLE, "Article"),
        (VIDEO, "Video"),
        (LAB, "Interactive lab"),
    ]

    course = models.ForeignKey(Course, related_name="lessons", on_delete=models.CASCADE)
    title = models.CharField(max_length=140)
    lesson_type = models.CharField(max_length=12, choices=LESSON_TYPES, default=ARTICLE)
    order = models.PositiveIntegerField(default=1)
    duration = models.CharField(max_length=30, default="10 min")
    content = models.TextField(help_text="Lesson text or instructions.")
    video_url = models.URLField(blank=True)
    challenge_prompt = models.TextField(blank=True)
    expected_answer = models.CharField(
        max_length=160,
        blank=True,
        help_text="For labs, the correct answer is checked on the server and never shown to learners.",
    )

    class Meta:
        ordering = ["order", "id"]

    def __str__(self):
        return f"{self.course.title}: {self.title}"


class Enrollment(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="enrollments", on_delete=models.CASCADE
    )
    course = models.ForeignKey(Course, related_name="enrollments", on_delete=models.CASCADE)
    enrolled_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-enrolled_at"]
        constraints = [
            models.UniqueConstraint(fields=["user", "course"], name="unique_course_enrollment")
        ]

    def __str__(self):
        return f"{self.user} — {self.course}"


class LessonProgress(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, related_name="lesson_progress", on_delete=models.CASCADE
    )
    lesson = models.ForeignKey(Lesson, related_name="progress_records", on_delete=models.CASCADE)
    completed_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-completed_at"]
        constraints = [
            models.UniqueConstraint(fields=["user", "lesson"], name="unique_lesson_progress")
        ]

    def __str__(self):
        return f"{self.user} completed {self.lesson}"
