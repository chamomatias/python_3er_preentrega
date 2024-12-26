from django.urls import path
from app import views

urlpatterns = [
    path('index/', views.index, name="index"),
    path('inicio/', views.inicio, name="inicio"),
    path('nuestra_historia/', views.nuestra_historia, name="nuestra_historia"),
    path('nosotros/', views.nosotros, name="nosotros"),
    path('productos/', views.productos, name="productos")
]

form_html = [
    path('form_Contactos/', views.form_Contactos, name="form_Contactos"),
    path('form_Rrhh/', views.form_Rrhh, name='form_Rrhh'),
]

urlpatterns += form_html

