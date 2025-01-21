from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('autori/', views.autori, name="autori"),
    path('vydavatelia/', views.vydavatelia, name="vydavatelia"),
    path('miesta/', views.miesta, name="miesta"),
    path('knihy/', views.knihy, name="knihy")
]