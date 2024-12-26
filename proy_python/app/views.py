# views.py
from django.shortcuts import render  # Asegúrate de importar render
from app.models import form_Contactos

def index(request):
    return render(request, "app/index.html")

def inicio(request):
    return render(request, "app/inicio.html")

def nuestra_historia(request):
    return render(request, "app/nuestra_historia.html")

def nosotros(request):
    return render(request, "app/nosotros.html")

def productos(request):
    return render(request, "app/productos.html")

def form_Rrhh(request):
    return render(request, 'app/form_Rrhh.html')


def form_Contactos(request):
    return render(request, 'app/form_Contactos.html')
