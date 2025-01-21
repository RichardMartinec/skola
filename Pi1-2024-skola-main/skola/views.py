from django.shortcuts import render, HttpResponse
from . models import *

# Create your views here.


def index(request):
    studenti = Student.objects.all()
    ucitelia = Teacher.objects.all()
    triedy = Class.objects.all()
    return render(request, 'skola/index.html', {'studenti': studenti , 'ucitelia': ucitelia, 'triedy': triedy})

def list_students(request):
    studenti = Student.objects.all()
    return render(request, 'skola/list_students.html', {'studenti': studenti})

def list_teachers(request):
    ucitelia = Teacher.objects.all()
    return render(request, 'skola/list_teachers.html', {'ucitelia': ucitelia})

def list_classes(request):
    triedy = Class.objects.all()
    return render(request, 'skola/list_classes.html', {'triedy': triedy})
    