from django.urls import path
from .views import *

urlpatterns = [
    path("", inicio, name = "Inicio"),
    path("formUsuario", formu, name = "FormularioUsuario"),
    path("formPeli", formuPeli, name = "FormPeli"),
    path("formSerie", formuSerie, name = "FormSerie"),
    path("buscar", buscarPeli, name = "Buscador"),
    path("resultados/", busqueda, name = "Resultado"),
]