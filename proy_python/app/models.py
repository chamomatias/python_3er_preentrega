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

class form_Contactos(models.Model):
    nombre_completo = models.CharField(max_length=40)
    correo_electronico = models.CharField(max_length=40)
    telefono = models.CharField(max_length=40)
    escribrenos = models.CharField(max_length=400)   
    def __str__(self):
        return f"{self.id} | {self.nombre_completo} | {self.correo_electronico} | {self.telefono} | {self.escribrenos}"
from django.db import models

class form_Rrhh(models.Model):
    nombre_completo = models.CharField(max_length=100)
    correo_electronico = models.EmailField()
    telefono = models.CharField(max_length=15)
    cv = models.FileField(upload_to='cvs/')  # Almacena los CVs en la carpeta 'media/cvs/'
    def __str__(self):
        return f"{self.nombre_completo} - {self.correo_electronico}"

