from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.db.models import Count, F, Prefetch, Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST

from .forms import LabAnswerForm, RegistrationForm
from .models import Course, Enrollment, Lesson, LessonProgress


def home(request):
    featured_courses = Course.objects.filter(published=True, featured=True)[:3]
    return render(request, "learning/home.html", {"featured_courses": featured_courses})


def catalog(request):
    courses = Course.objects.filter(published=True).annotate(
        lesson_count=Count("lessons")
    )
    query = request.GET.get("q", "").strip()
    category = request.GET.get("category", "").strip()
    semester = request.GET.get("semester", "").strip()
    if query:
        courses = courses.filter(
            Q(title__icontains=query)
            | Q(summary__icontains=query)
            | Q(module_code__icontains=query)
        )
    if category:
        courses = courses.filter(category=category)
    if semester in {str(value) for value, _ in Course.SEMESTER_CHOICES}:
        courses = courses.filter(semester=int(semester))
    courses = courses.order_by(F("semester").asc(nulls_last=True), "module_code", "title")
    categories = (
        Course.objects.filter(published=True)
        .order_by("category")
        .values_list("category", flat=True)
        .distinct()
    )
    return render(
        request,
        "learning/catalog.html",
        {
            "courses": courses.distinct(),
            "categories": categories,
            "semester_choices": Course.SEMESTER_CHOICES,
            "diploma_module_count": Course.objects.filter(
                published=True, semester__isnull=False
            ).count(),
            "query": query,
            "selected_category": category,
            "selected_semester": semester,
        },
    )


@login_required
def dashboard(request):
    enrollments = (
        Enrollment.objects.filter(user=request.user)
        .select_related("course")
        .prefetch_related("course__lessons")
    )
    enrollment_cards = []
    completed_total = 0
    completed_lesson_ids = set(
        LessonProgress.objects.filter(user=request.user).values_list(
            "lesson_id", flat=True
        )
    )
    for enrollment in enrollments:
        lessons = list(enrollment.course.lessons.all())
        lesson_ids = {lesson.id for lesson in lessons}
        completed_count = len(lesson_ids & completed_lesson_ids)
        lesson_count = len(lessons)
        completed_total += completed_count
        next_lesson = next(
            (lesson for lesson in lessons if lesson.id not in completed_lesson_ids),
            lessons[-1] if lessons else None,
        )
        enrollment_cards.append(
            {
                "course": enrollment.course,
                "completed": completed_count,
                "total": lesson_count,
                "percent": round(completed_count * 100 / lesson_count) if lesson_count else 0,
                "next_lesson": next_lesson,
            }
        )
    badges = []
    if completed_total >= 1:
        badges.append({"icon": "✳", "name": "First steps", "description": "Complete your first lesson"})
    if completed_total >= 5:
        badges.append({"icon": "⌘", "name": "Curious mind", "description": "Complete five lessons"})
    if completed_total >= 10:
        badges.append({"icon": "⬡", "name": "Cyber scholar", "description": "Complete ten lessons"})
    return render(
        request,
        "learning/dashboard.html",
        {
            "enrollment_cards": enrollment_cards,
            "completed_total": completed_total,
            "badges": badges,
        },
    )


def course_detail(request, slug):
    course = get_object_or_404(
        Course.objects.filter(published=True).prefetch_related(
            Prefetch("lessons", queryset=Lesson.objects.order_by("order", "id"))
        ),
        slug=slug,
    )
    enrolled = request.user.is_authenticated and Enrollment.objects.filter(
        user=request.user, course=course
    ).exists()
    completed_ids = set()
    if enrolled:
        completed_ids = set(
            LessonProgress.objects.filter(
                user=request.user, lesson__course=course
            ).values_list("lesson_id", flat=True)
        )
    lessons = list(course.lessons.all())
    next_lesson = next(
        (lesson for lesson in lessons if lesson.id not in completed_ids),
        lessons[-1] if lessons else None,
    )
    completed_count = len(completed_ids)
    lesson_count = len(lessons)
    return render(
        request,
        "learning/course_detail.html",
        {
            "course": course,
            "enrolled": enrolled,
            "completed_ids": completed_ids,
            "first_lesson": next_lesson,
            "completed_count": completed_count,
            "lesson_count": lesson_count,
            "progress_percent": (
                round(completed_count * 100 / lesson_count) if lesson_count else 0
            ),
        },
    )


@login_required
@require_POST
def enroll(request, slug):
    course = get_object_or_404(Course, slug=slug, published=True)
    Enrollment.objects.get_or_create(user=request.user, course=course)
    messages.success(request, f"You’re enrolled in {course.title}.")
    return redirect("course_detail", slug=course.slug)


@login_required
def lesson_detail(request, slug, lesson_id):
    course = get_object_or_404(Course, slug=slug, published=True)
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        messages.info(request, "Enroll in this course to start its lessons.")
        return redirect("course_detail", slug=course.slug)
    lesson = get_object_or_404(Lesson, course=course, pk=lesson_id)
    completed = LessonProgress.objects.filter(user=request.user, lesson=lesson).exists()
    learning_context = _lesson_navigation_context(request.user, course, lesson)
    return render(
        request,
        "learning/lesson_detail.html",
        {
            "course": course,
            "lesson": lesson,
            "completed": completed,
            **learning_context,
        },
    )


def _lesson_navigation_context(user, course, lesson):
    lessons = list(course.lessons.all())
    lesson_index = next(
        (index for index, item in enumerate(lessons) if item.id == lesson.id),
        0,
    )
    completed_ids = set(
        LessonProgress.objects.filter(user=user, lesson__course=course).values_list(
            "lesson_id", flat=True
        )
    )
    return {
        "answer_form": LabAnswerForm(),
        "path_lessons": lessons,
        "completed_ids": completed_ids,
        "room_number": lesson_index + 1,
        "room_count": len(lessons),
        "previous_lesson": lessons[lesson_index - 1] if lesson_index else None,
        "next_lesson": (
            lessons[lesson_index + 1] if lesson_index + 1 < len(lessons) else None
        ),
        "path_progress": (
            round(len(completed_ids) * 100 / len(lessons)) if lessons else 0
        ),
    }


@login_required
@require_POST
def complete_lesson(request, slug, lesson_id):
    course = get_object_or_404(Course, slug=slug, published=True)
    if not Enrollment.objects.filter(user=request.user, course=course).exists():
        messages.error(request, "Enroll in this course before completing lessons.")
        return redirect("course_detail", slug=course.slug)
    lesson = get_object_or_404(Lesson, course=course, pk=lesson_id)
    if lesson.lesson_type == Lesson.LAB:
        form = LabAnswerForm(request.POST)
        if not form.is_valid():
            learning_context = _lesson_navigation_context(
                request.user, course, lesson
            )
            return render(
                request,
                "learning/lesson_detail.html",
                {
                    "course": course,
                    "lesson": lesson,
                    "completed": False,
                    **learning_context,
                    "answer_form": form,
                },
            )
        expected = " ".join(lesson.expected_answer.casefold().split())
        submitted = " ".join(form.cleaned_data["answer"].casefold().split())
        if not expected or submitted != expected:
            messages.error(request, "Not quite. Review the scenario and try again.")
            return redirect("lesson_detail", slug=course.slug, lesson_id=lesson.id)
    LessonProgress.objects.get_or_create(user=request.user, lesson=lesson)
    messages.success(request, "Lesson completed. Nice work!")
    return redirect("lesson_detail", slug=course.slug, lesson_id=lesson.id)


def register(request):
    if request.user.is_authenticated:
        return redirect("dashboard")
    form = RegistrationForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        messages.success(request, "Welcome aboard. Your learning journey starts here.")
        return redirect("dashboard")
    return render(request, "registration/register.html", {"form": form})
