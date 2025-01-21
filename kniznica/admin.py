from django.contrib import admin
from .models import Autor, Vydavatel, Miesto, Kniha

admin.site.register(Autor)
admin.site.register(Vydavatel)
admin.site.register(Miesto)
admin.site.register(Kniha)
