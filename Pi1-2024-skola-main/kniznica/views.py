from django.shortcuts import render, HttpResponse
from . models import *

# Create your views here.

def index(request):
    knihy = Kniha.objects.all()
    autori = Autor.objects.all()
    vydavatelia = Vydavatel.objects.all()
    miesta = Miesto.objects.all()
    return render(request, 'kniznica/index.html', {'knihy': knihy, 'autori': autori, 'vydavatelia': vydavatelia, 'miesta': miesta})

def knihy(request):
    knihy = Kniha.objects.all()
    return render(request, 'kniznica/knihy.html', {'knihy': knihy})
    
def autori(request):
    autori = Autor.objects.all()
    return render(request, 'kniznica/autori.html', {'autori': autori})
    
def vydavatelia(request):
    vydavatelia = Vydavatel.objects.all()
    return render(request, 'kniznica/vydavatelia.html', {'vydavatelia': vydavatelia})
    
def miesta(request):
    miesta = Miesto.objects.all()
    return render(request, 'kniznica/miesta.html', {'miesta': miesta})