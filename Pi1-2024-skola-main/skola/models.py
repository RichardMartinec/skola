from django.db import models

# Create your models here.

class Class(models.Model):
    nazov = models.CharField(max_length=10)

    def __str__(self):
        return f"{self.nazov}"

    class Meta:
        verbose_name = "Trieda"
        verbose_name_plural = "Triedy"
        ordering = ['nazov']

class Student(models.Model):
    meno = models.CharField(max_length=20) # textové pole
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.trieda:
            trieda = self.trieda
        else:
            trieda = ""
        return f"{self.meno} {self.priezvisko} {trieda}"
    
    class Meta:
        verbose_name = "Študent"
        verbose_name_plural = "Študenti"
        ordering = ['priezvisko']
    

class Teacher(models.Model):
    titul = models.CharField(max_length=10)
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)
    trieda = models.ForeignKey(Class, on_delete=models.SET_NULL, null=True, blank=True)

    def __str__(self):
        if self.trieda:
            trieda = self.trieda
        else:
            trieda = ""
        return f"{self.titul} {self.meno} {self.priezvisko} {trieda}"
    
    class Meta:
        verbose_name = "Učiteľ"
        verbose_name_plural = "Učitelia"
        ordering = ['priezvisko']