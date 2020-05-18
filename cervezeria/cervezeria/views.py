from django.http import HttpResponse
from django.shortcuts import render
from polls.models import TipoCerveza, NombreCerveza, MarcaCerveza
from django.core.mail import EmailMessage
from cervezeria.forms import ContactoForm
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
#def hola(request):
#    return HttpResponse("hola mundo prueba")

def index(request):
    return render(request, 'index.html')

def cervezas(request):
    cervezas=NombreCerveza.objects.all()
    contexto = {
    'cervezas':cervezas
    }
    return render(request, 'cervezas.html', contexto)

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

def usuario_nuevo(request):
    if request.method == 'POST':
        formulario = UserCreationForm(request.POST)
        try:
            formulario.save()
            return render(request, 'usuario_agregado.html')
        except:
            return render(request, 'usuario_no_agregado.html')
    else:
        formulario=UserCreationForm()
        return render(request, 'usuario_nuevo.html', {'formulario':formulario})

@login_required(login_url='/ingresar')
def privado(request):
    usuario=request.user
    return render(request, 'privado.html',{'usuario':usuario})

def ingresar(request):
    if not request.user.is_anonymous:
        return HttpResponseRedirect('privado')
    elif request.method=='POST':
        formulario = AuthenticationForm(request.POST)
        if formulario.is_valid:
            usuario = request.POST['username']
            clave = request.POST['password']
            acceso= authenticate(username=usuario, password=clave)
            if acceso is not None:
                if acceso.is_active:
                    login(request, acceso)
                    return HttpResponseRedirect('/privado')
                else:
                    return render(render, 'no_activo.html')
            else:
                return render(request, 'no_usuario.html')
    else:
        formulario=AuthenticationForm()
        return render(request, 'ingresar.html', {'formulario':formulario})

def salir(request):
    if not request.user.is_anonymous:
        logut(request)
        return HttpResponseRedirect('/ingresar')
    else:
        return render(request, 'no_logueado.html')

def error_404(request, exception):
    response = render(request, '404.html', {})
    return response

def error_500(request):
    response = render(request, '500.html', {})
    return response
