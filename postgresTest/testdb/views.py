from django.shortcuts import render
from .models import Teacher

# Create your views here.

def showTeachers(request):
    teachers = Teacher.objects.all()

    return render(request, 'testdb/teachers.html', {'teachers': teachers})
