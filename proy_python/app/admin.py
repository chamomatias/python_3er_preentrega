from django.contrib import admin
from .models import unidad_de_negocio, producto, cliente


# Register your models here.
@admin.register(unidad_de_negocio)
class unidad_de_negocioAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "provincia")
    ordering = ("id","nombre", "provincia")

@admin.register(producto)
class productoAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "unidad_de_negocio")
    ordering = ("id","nombre", "unidad_de_negocio")

@admin.register(cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nombre", "unidad_de_negocio")
    ordering = ("id","nombre", "unidad_de_negocio")