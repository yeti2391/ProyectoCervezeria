from django.http import HttpResponse
from django.shortcuts import render
from polls.models import TipoCerveza, NombreCerveza, MarcaCerveza
from django.core.mail import EmailMessage
from cervezeria.forms import ContactoForm

#def hola(request):
#    return HttpResponse("hola mundo prueba")

def index(request):
    return render(request, 'index.html')

def cervezas(request):
    return render(request, 'cervezas.html')

def brevehistoria(request):
    return render(request, 'brevehistoria.html')

def acerca(request):
    return render(request, 'acerca.html')

def buscar(request):
    if "busca" in request.GET and request.GET["busca"]:
        consulta= request.GET["busca"]
        NombreCerveza = NombreCerveza.objects.filter(titulo__icontains = consulta)
        return render (request, 'resultados.html', {'res': valor})
    else:
        return render (request, 'resultados.html')

def contacto(request):
    if request.method == 'POST':
        formulario = ContactoForm(request.POST)
        if formulario.is_valid():
            titulo = "Correo desde El Choborra"
            contenido = formulario.cleaned_data['mensaje'] + '\n\n'
            contenido += 'comunicarse al correo' + formulario.cleaned_data['correo']
            correo = EmailMessage(titulo, contenido, to=['elchoborra2391@gmail.com'])
            try:
                correo.send()
                return render(request, 'correo_enviado.html') # PROBAR AGREGAR TARGET BLNAK PARA Q SE ABRA EN OTRA PESTANA
            except:
                return render(request, 'correo_no_enviado.html') #Y ESTE también
    else:
        formulario = ContactoForm()
        return render (request, 'contacto.html', {'formulario': formulario})
