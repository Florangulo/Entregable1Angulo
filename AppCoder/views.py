from django.shortcuts import render
from django.http import HttpResponse
from AppCoder.forms import *
from .models import *

def inicio(request):
    return render(request, "AppCoder/inicio.html")

def formu(request):
    if request.method == "POST":
        formulario1 = Formulario(request.POST)
        if formulario1.is_valid():
            info = formulario1.cleaned_data
            usuarioF = Usuario(nombre = info["nombre"], apellido = info["apellido"], correo = info["mail"])
            usuarioF.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario1 = Formulario()
    return render(request, "AppCoder/formUsuario.html", {"form1":formulario1})

def formuPeli(request):
    if request.method == "POST":
        formulario2 = PeliForm(request.POST)
        if formulario2.is_valid():
            info = formulario2.cleaned_data
            peliF = Peli(titulo = info["titulo"], genero = info["genero"], anio = info["anio"])
            peliF.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario2 = PeliForm()
    return render(request, "AppCoder/formPeli.html", {"form2":formulario2})

def formuSerie(request):
    if request.method == "POST":
        formulario3 = SerieForm(request.POST)
        if formulario3.is_valid():
            info = formulario3.cleaned_data
            serieF = Serie(titulo = info["titulo"], genero = info["genero"], anio = info["anio"])
            serieF.save()
            return render(request, "AppCoder/inicio.html")
    else:
        formulario3 = SerieForm()
    return render(request, "AppCoder/formSerie.html", {"form3":formulario3})

def buscarPeli(request):
    return render(request, "AppCoder/formBuscador.html")

def busqueda(request):
    if request.GET["titulo"]:
        buscar = request.GET["titulo"]
        pelis = Peli.objects.filter(titulo__icontains=buscar)
        return render(request, "AppCoder/resultados.html", {"pelis":pelis, "buscar":buscar})
    else:
        mensaje = "No enviaste datos."
    return HttpResponse(mensaje)