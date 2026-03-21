# urls.py
from django.urls import path
from .views import student_create, student_list

urlpatterns = [
    path('students/', student_list, name='student_list'),
    path('students/add/', student_create, name='student_create'),
]