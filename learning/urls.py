from django.contrib.auth import views as auth_views
from django.urls import path

from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("courses/", views.catalog, name="catalog"),
    path("courses/<slug:slug>/", views.course_detail, name="course_detail"),
    path("courses/<slug:slug>/enroll/", views.enroll, name="enroll"),
    path("courses/<slug:slug>/lessons/<int:lesson_id>/", views.lesson_detail, name="lesson_detail"),
    path(
        "courses/<slug:slug>/lessons/<int:lesson_id>/complete/",
        views.complete_lesson,
        name="complete_lesson",
    ),
    path("dashboard/", views.dashboard, name="dashboard"),
    path("register/", views.register, name="register"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="registration/login.html"),
        name="login",
    ),
    path("logout/", auth_views.LogoutView.as_view(), name="logout"),
]
