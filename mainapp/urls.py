from django.urls import path

from mainapp import views
from mainapp.apps import MainappConfig

app_name = MainappConfig.name

urlpatterns = [
    path("", views.MainPageView.as_view(), name="main_page"),
    path("categories/", views.CategoriesPageView.as_view(), name="categories"),
    path("categories/<int:pk>/", views.CategoryCoursesPageView.as_view(), name="category_courses"),
    path("course/<int:pk>/", views.CourseDetailPageView.as_view(), name="course_detail"),
    path("lesson/<int:pk>/", views.LessonDetailPageView.as_view(), name="lesson_detail"),
    path("login/", views.LoginPageView.as_view(), name="login"),
    path("about/", views.AboutPageView.as_view(), name="about"),
    path("news/", views.NewsPageView.as_view(), name="news"),
    path("register/", views.RegisterPageView.as_view(), name="register"),
]
