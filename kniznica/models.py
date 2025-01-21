from django.db import models

# Create your models here.

class Autor(models.Model):
    meno = models.CharField(max_length=20)
    priezvisko = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.meno} {self.priezvisko}"
    
    class Meta:
        verbose_name = "Autor"
        verbose_name_plural = "Autori"
        ordering = ['priezvisko']

class Vydavatel(models.Model):
    nazov = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Vydavatel"
        verbose_name_plural = "Vydavatelia"
        ordering = ["nazov"]

class Miesto(models.Model):
    nazov = models.CharField(max_length=20)

    def __str__(self):
        return f"{self.nazov}"
    
    class Meta:
        verbose_name = "Miesto"
        verbose_name_plural = "Miesta"
        ordering = ["nazov"]

class Kniha(models.Model):
    autor = models.ForeignKey(Autor, on_delete=models.SET_NULL, null=True, blank=True)
    vydavatel = models.ForeignKey(Vydavatel, on_delete=models.SET_NULL, null=True, blank=True)
    miesto = models.ForeignKey(Miesto, on_delete=models.SET_NULL, null=True, blank=True)
    nazov = models.CharField(max_length=30)
    rok = models.IntegerField()

    def __str__(self):
        return f"{self.autor} {self.vydavatel} {self.miesto} {self.nazov} {self.rok}"
    
    class Meta:
        verbose_name = "Kniha"
        verbose_name_plural = "Knihy"
        ordering = ["nazov"]
