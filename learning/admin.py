from django.contrib import admin

from .models import Course, Enrollment, Lesson, LessonProgress


class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 0
    fields = ("order", "title", "lesson_type", "duration")


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "level", "published", "featured")
    list_filter = ("published", "featured", "level", "category")
    search_fields = ("title", "summary")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [LessonInline]


@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ("title", "course", "lesson_type", "order")
    list_filter = ("lesson_type", "course")
    search_fields = ("title", "course__title")


@admin.register(Enrollment)
class EnrollmentAdmin(admin.ModelAdmin):
    list_display = ("user", "course", "enrolled_at")
    list_filter = ("course",)
    search_fields = ("user__username", "course__title")


@admin.register(LessonProgress)
class LessonProgressAdmin(admin.ModelAdmin):
    list_display = ("user", "lesson", "completed_at")
    list_filter = ("lesson__course",)
    search_fields = ("user__username", "lesson__title")
