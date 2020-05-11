from django.http import HttpResponse
from django.shortcuts import render

#def hola(request):
#    return HttpResponse("hola mundo prueba")

def index(request):
    return render(request, 'index.html')

def cervezas(request):
    return render(request, 'cervezas.html')

def brevehistoria(request):
    return render(request, 'brevehistoria.html')
