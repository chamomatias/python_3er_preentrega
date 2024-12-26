from django.db import models

# Create your models here.
class unidad_de_negocio(models.Model):
    nombre = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)
    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.provincia}"

class producto(models.Model):
    nombre = models.CharField(max_length=40)
    unidad_de_negocio = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.unidad_de_negocio}"

class cliente(models.Model):
    nombre = models.CharField(max_length=40)
    unidad_de_negocio = models.CharField(max_length=20)
    def __str__(self):
        return f"{self.id} | {self.nombre} | {self.unidad_de_negocio}"
