from django.contrib import admin
from .models import unidad_de_negocio, producto, cliente


# Register your models here.
admin.site.register(unidad_de_negocio)

admin.site.register(producto)
admin.site.register(cliente)