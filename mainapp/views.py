from django.views.generic import TemplateView
from django.shortcuts import get_object_or_404

class MainPageView(TemplateView):
    template_name = "mainapp/index.html"


class AboutPageView(TemplateView):
    template_name = "mainapp/about.html"


class CategoriesPageView(TemplateView):
    template_name = "mainapp/categories.html"


class LoginPageView(TemplateView):
    template_name = "mainapp/login.html"


class RegisterPageView(TemplateView):
    template_name = "mainapp/register.html"


class CategoryCoursesPageView(TemplateView):
    template_name = "mainapp/category_courses.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        return context


class CourseDetailPageView(TemplateView):
    template_name = "mainapp/course_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        return context


class LessonDetailPageView(TemplateView):
    template_name = "mainapp/lesson_detail.html"

    def get_context_data(self, pk=None, **kwargs):
        context = super().get_context_data(pk=pk, **kwargs)
        return context


class NewsPageView(TemplateView):
    template_name = "mainapp/news.html"
