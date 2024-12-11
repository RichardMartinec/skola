from django.shortcuts import render, HttpResponse
from . models import * # naimportovanie všetkých modelov z models.py

def index(request):
    studenti = Student.objects.all()
    return HttpResponse(studenti)
