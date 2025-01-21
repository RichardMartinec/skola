from django.shortcuts import render, HttpResponse
from . models import *

def autori(request):
    autori = Autor.objects.all()
    return render(request, "kniznica/index.html", {"autori":autori,})

def vydavatelia(request):
    vydavatelia = Vydavatel.objects.all()
    return render(request, "kniznica/index.html", {"vydavatelia":vydavatelia,})

def miesta(request):
    miesta = Miesto.objects.all()
    return render(request, "kniznica/index.html", {"miesta": miesta,})

def knihy(request):
    knihy = Kniha.objects.all()
    return render(request, "kniznica/index.html", {"knihy":knihy})

def index(request):
    autori = Autor.objects.all()
    vydavatelia = Vydavatel.objects.all()
    miesta = Miesto.objects.all()
    knihy = Kniha.objects.all()
    return render(request, "kniznica/index.html", {"autori":autori, "vydavatelia":vydavatelia, "miesta": miesta, "knihy":knihy})
