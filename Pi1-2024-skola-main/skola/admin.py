from django.contrib import admin
from .models import Student, Teacher, Class

# Register your models here.

admin.site.register(Class)
admin.site.register(Student)
admin.site.register(Teacher)