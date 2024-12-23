# views.py
from django.shortcuts import render  # Asegúrate de importar render

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

def contactos(request):
    return render(request, "app/contactos.html")
