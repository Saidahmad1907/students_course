from django.urls import path
from . import views

urlpatterns = [
    path('', views.courses_and_students, name='courses_and_students'),
    path('course/<int:course_id>/', views.course_students, name='course_students'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),
    path('', views.home, name='home'),
]

