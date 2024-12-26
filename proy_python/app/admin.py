from django.contrib import admin
from app.models import unidad_de_negocio, producto, cliente

# Register your models here.
@admin.register(unidad_de_negocio)
class unidad_de_negocioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'provincia')
    search_fields = ('nombre', 'provincia')

admin.site.register(producto)
class productoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'unidad_de_negocio')
    search_fields = ('nombre', 'unidad_de_negocio')

admin.site.register(cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'unidad_de_negocio')
    search_fields = ('nombre', 'unidad_de_negocio')