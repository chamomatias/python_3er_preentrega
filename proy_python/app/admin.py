from django.contrib import admin
from app.models import unidad_de_negocio, producto, cliente, Contactos

# Register your models here.
admin.register(unidad_de_negocio)
class unidad_de_negocioAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'provincia')
    search_fields = ('nombre', 'provincia')
    list_editable = ('nombre', 'provincia')
    list_filter = ('nombre', 'provincia')

admin.site.register(producto)
class productoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'unidad_de_negocio')
    search_fields = ('nombre', 'unidad_de_negocio')
    list_editable = ('nombre', 'unidad_de_negocio')
    list_filter = ('nombre', 'unidad_de_negocio')

admin.site.register(cliente)
class clienteAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre', 'unidad_de_negocio')
    search_fields = ('nombre', 'unidad_de_negocio')
    list_editable = ('nombre', 'unidad_de_negocio')
    list_filter = ('nombre', 'unidad_de_negocio')

admin.site.register(Contactos)
class ContactosAdmin(admin.ModelAdmin):
    list_display = ('id', 'nombre_completo', 'correo_electronico', 'telefono', 'escribrenos')
    search_fields = ('nombre_completo', 'correo_electronico', 'telefono', 'escribrenos')
    list_editable = ('nombre_completo', 'correo_electronico', 'telefono', 'escribrenos')
    list_filter = ('nombre_completo', 'correo_electronico', 'telefono', 'escribrenos')