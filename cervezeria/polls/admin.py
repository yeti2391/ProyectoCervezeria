from django.contrib import admin
from polls.models import TipoCerveza, NombreCerveza, MarcaCerveza, Origen
# Register your models here.
admin.site.register(TipoCerveza)
admin.site.register(NombreCerveza)
admin.site.register(MarcaCerveza)
admin.site.register(Origen)
