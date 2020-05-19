from django.db import models

# Create your models here.

class TipoCerveza(models.Model):
    id = models.AutoField(primary_key=True)
    tipo=models.CharField(max_length=30, blank=False, null= False )

    class Meta:
        ordering=["tipo"]
        verbose_name= 'Tipo'
        verbose_name_plural = "Tipos"

    def __str__(self):
        return self.tipo

class MarcaCerveza(models.Model):
    id = models.AutoField(primary_key=True)
    marca=models.CharField(max_length=50, blank=True, null= True)
    pais=models.CharField(max_length=50)
    sitioweb=models.URLField(blank=True, null=True)

    class Meta:
        ordering=["marca"]
        verbose_name= 'marca'
        verbose_name_plural = "marcas"

    def __str__(self):
        return self.marca

class NombreCerveza(models.Model):
    tipo=models.OneToOneField(TipoCerveza, null=True, on_delete=models.CASCADE)
    #marca=models.OneToOneField(MarcaCerveza, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30, blank=False, null= False)
    color=models.CharField(max_length=30, blank=False, null= False)
    descripcion=models.CharField(max_length=300)

    class Meta:
        ordering=["tipo"]
        verbose_name= 'cerveza'
        verbose_name_plural = "cervezas"

    def __str__(self):
        return "%s %s %s %s" % (self.tipo, self.nombre, self.color, self.descripcion)
