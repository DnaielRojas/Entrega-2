from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    return render(request, 'Dulces.html', {})

def productos(request):
    return render(request, 'productos.html', {})

def recuperar(request):
    return render(request, 'recuperar.html', {})

def gestion_usuarios(request):
    return render(request, 'gestion_usuarios.html', {})

def modificar_usuario(request):
    return render(request, 'modificar_usuario.html', {})

def solicitud(request):
    return render(request, 'solicitud.html', {})