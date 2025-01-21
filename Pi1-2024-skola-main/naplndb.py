import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()

from skola.models import *
import random


Class.objects.all().delete()
Student.objects.all().delete()
Teacher.objects.all().delete()

for rocnik in range(1,5):
    for pismeno in ["A", "B", "C", "D"]:
        Class.objects.create(nazov=f"{rocnik}.{pismeno}")

for meno in ["Ján", "Adam", "Jozef", "Tomáš"]:
    for priezvisko in ["Mrkvička", "Šarlina", "Šutek", "Trnka"]:
        Student.objects.create(meno=meno, priezvisko=priezvisko, trieda=random.choice(Class.objects.all())) 
        titul = random.choice(["Mgr.", "Ing.", "PhDr."])
        Teacher.objects.create(titul=titul, meno=meno, priezvisko=priezvisko, trieda=random.choice(Class.objects.all()))
