from django.http import HttpResponse
from django.shortcuts import render

#def hola(request):
#    return HttpResponse("hola mundo prueba")

def index(request):
    return render(request, 'index.html')
