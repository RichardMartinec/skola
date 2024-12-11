import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
import django
django.setup()

from skola.models import *
import random

Trieda.objects.all().delete() # vymaže všetky záznamy v tabulke Tried
Student.objects.all().delete()
Ucitel.objects.all().delete()

# Trieda.objects.create(nazov=f"I.A") #vytvorí záznam v tabuľke Tried
triedy = []
for rocnik in range(1,5):
    for pismeno in ['A','B','C','D']:
        Trieda.objects.create(nazov=f"{rocnik}.{pismeno}")


for meno in ["Adam","Michal","Jozef","Ondrej"]:
    for priezvisko in ["Stachoň","Šarlina","Šimek","Trnka"]:
        Student.objects.create(meno=meno, priezvisko=priezvisko)

for ucitel in ["Adam","Michal","Jozef","Ondrej"]:
    for priezvisko in ["Stachoň","Šarlina","Šimek","Trnka"]:
        titul = random.choice(["Mgr.", "Ing.", "PhDr."])
        Ucitel.objects.create(titul=titul, meno=meno, priezvisko=priezvisko)