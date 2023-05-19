from django.shortcuts import render, get_object_or_404
from .models import Course
# Create your views here.

def index(request):
    courses = Course.objects.all()
    return render(request, 'shop/courses.html', {'course': courses})

def single_course(request, course_id):
    course = get_object_or_404(Course, pk=course_id)
    return render(request, 'shop/single_course.html', {'course': course})