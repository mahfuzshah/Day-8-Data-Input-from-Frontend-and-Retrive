
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.StudentPage, name='student'),
    path('teacher', views.TeacherPage, name='teacher'),
]