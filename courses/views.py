from django.shortcuts import render

# Create your views here.

from django.shortcuts import render, get_object_or_404
from .models import Course, Student

def courses_and_students(request):
    courses = Course.objects.all()
    students = Student.objects.all()
    return render(request, 'courses_and_students.html', {'courses': courses, 'students': students})

def course_students(request, course_id):
    course = get_object_or_404(Course, id=course_id)
    students = course.students.all()
    return render(request, 'course_students.html', {'course': course, 'students': students})

def student_detail(request, student_id):
    student = get_object_or_404(Student, id=student_id)
    return render(request, 'student_detail.html', {'student': student})

from django.shortcuts import render

def home(request):
    return render(request, 'home.html')
