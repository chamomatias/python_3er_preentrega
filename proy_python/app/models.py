from django.db import models

# Create your models here.
from django.db import models

# Create your models here.
class unidad_de_negocio(models.Model):
    nombre = models.CharField(max_length=40)
    provincia = models.CharField(max_length=40)

class producto(models.Model):
    nombre = models.CharField(max_length=40)
    unidad_de_negocio = models.CharField(max_length=20)

class cliente(models.Model):
    nombre = models.CharField(max_length=40)
    unidad_de_negocio = models.CharField(max_length=20)
