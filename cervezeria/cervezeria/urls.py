"""cervezeria URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import include, path
from cervezeria.views import *
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import handler404, handler500
#from cervezeria.views import hola



handler404=error_404
handler500=error_500

urlpatterns = [
    path('admin/', admin.site.urls),
    #path('hola/', hola),
    path('', index, name='inicio'),
    path('cervezas/', cervezas, name='cervezas'),
    path('brevehistoria/', brevehistoria, name='brevehistoria'),
    path('acerca/', acerca, name='acerca'),
    path('buscar/', buscar, name='buscar'),
    path('contacto/', contacto, name='contacto'),
    path('registro/', usuario_nuevo, name='registro'),
    path('privado/', privado),
    path('ingresar/', ingresar, name='ingresar'),
    path('salir/', salir, name='salir'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
