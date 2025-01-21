from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('studenti/', views.list_students, name='list_students'),
    path('ucitelia/', views.list_teachers, name='list_teachers'),
    path('triedy/', views.list_classes, name='list_classes'),
]