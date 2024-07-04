# alumnos/views.py

from django.shortcuts import render

def inicio(request):
    return render(request, 'alumnos/inicio.html')

def index(request):
    return render(request, 'alumnos/index.html')

def compra(request):
    return render(request, 'alumnos/compra.html')

def envivo(request):
    return render(request, 'alumnos/envivo.html')

def info(request):
    return render(request, 'alumnos/info.html')

def resena(request):
    return render(request, 'alumnos/resena.html')


def login(request):
    # Aquí va la lógica de la vista de inicio de sesión
    return render(request, 'alumnos/login.html')