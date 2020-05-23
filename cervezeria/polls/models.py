from django.db import models

# Create your models here.

class TipoCerveza(models.Model):
    id = models.AutoField(primary_key=True)
    tipo=models.CharField(max_length=30, blank=False, null= False, default='None' )

    class Meta:
        ordering=["tipo"]
        verbose_name= 'Tipo'
        verbose_name_plural = "Tipos"

    def __str__(self):
        return self.tipo
class Origen(models.Model):
    pais=models.CharField(max_length=100)
    class Meta:
        ordering=["pais"]
        verbose_name="Pais"
        verbose_name_plural="Paises"
    def __str__(self):
        return self.pais

class MarcaCerveza(models.Model):
    id = models.AutoField(primary_key=True)
    marca=models.CharField(max_length=50, default='S/M')
    pais=models.ForeignKey(Origen, on_delete=models.CASCADE)
    sitioweb=models.URLField(blank=True, null=True)

    class Meta:
        ordering=["marca"]
        verbose_name= 'Marca'
        verbose_name_plural = "Marcas"

    def __str__(self):
        return self.marca

class NombreCerveza(models.Model):
    id=models.AutoField(primary_key=True)
    tipo=models.ForeignKey(TipoCerveza, default='None' , on_delete=models.CASCADE)
    marca=models.ForeignKey(MarcaCerveza, null=True, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30, blank=False, null= False)
    color=models.CharField(max_length=30, blank=False, null= False)
    descripcion=models.CharField(max_length=600)
    precio=models.CharField(max_length=4, null=True)
    foto=models.ImageField(upload_to='fotocerv', null=True)

    class Meta:
        ordering=["tipo"]
        verbose_name= 'Cerveza'
        verbose_name_plural = "Cervezas"

    def __str__(self):
        return "%s %s %s %s %s %s" % (self.tipo, self.marca, self.nombre, self.color, self.descripcion, self.precio)
