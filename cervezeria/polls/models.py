from django.db import models

# Create your models here.

class TipoCerveza(models.Model):
    tipo=models.CharField(max_length=30)

    class Meta:
        ordering=["tipo"]
        verbose_name_plural = "Tipos"

    def __str__(self):
        return self.tipo

class NombreCerveza(models.Model):
    tipo=models.ForeignKey(TipoCerveza, null=True, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30)
    color=models.CharField(max_length=30)
    descripcion=models.CharField(max_length=300)

    class Meta:
        ordering=["nombre"]
        verbose_name_plural = "Nombres"

    def __str__(self):
        return "%s %s %s" % (self.nombre, self.color, self.descripcion)

class MarcaCerveza(models.Model):
    marca=models.CharField(max_length=50)
    pais=models.CharField(max_length=50)
    sitioweb=models.URLField(blank=True, null=True)

    class Meta:
        ordering=["marca"]
        verbose_name_plural = "marcas"

    def __str__(self):
        return self.marca
