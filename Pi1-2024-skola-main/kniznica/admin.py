from django.contrib import admin
from .models import Kniha, Autor, Vydavatel, Miesto

# Register your models here.

admin.site.register(Kniha)
admin.site.register(Autor)
admin.site.register(Vydavatel)
admin.site.register(Miesto)