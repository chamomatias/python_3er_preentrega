# views.py
from django.shortcuts import render  # Asegúrate de importar render
from app.models import Contactos

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

def Contactos(request): #formulario de contacto

    if request.method == "POST":
        nombre_completo = request.POST["nombre_completo"]
        correo_electronico = request.POST["correo_electronico"]
        telefono = request.POST["telefono"]
        escribrenos = request.POST["escribrenos"]

        contacto = Contactos(nombre_completo=nombre_completo, correo_electronico=correo_electronico, telefono=telefono, escribrenos=escribrenos)
        contacto.save()
        return render(request, "app/Contactos.html", {"mensaje": "Contacto guardado correctamente"})

    return render(request, "app/Contactos.html")
