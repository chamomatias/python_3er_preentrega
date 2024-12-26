from django.contrib import admin
from app.models import unidad_de_negocio, producto, cliente, Contactos

# Register your models here.
@admin.register(unidad_de_negocio)
class unidad_de_negocioAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "provincia"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]


@admin.register(producto)
class productoAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "unidad_de_negocio"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]


@admin.register(cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre", "unidad_de_negocio"]
    search_fields = ["nombre"]
    list_filter = ["nombre"]


@admin.register(Contactos)
class ContactosAdmin(admin.ModelAdmin):
    list_display = ["id", "nombre_completo", "correo_electronico", "telefono", "escribrenos"]
    search_fields = ["nombre_completo", "correo_electronico"]