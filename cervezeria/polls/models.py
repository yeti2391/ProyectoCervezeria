from django.db import models

# Create your models here.

class TipoCerveza(models.Model):
    id = models.AutoField(primary_key=True)
    tipo=models.CharField(max_length=30, blank=False, null= True, unique=True )
    class Meta:
        ordering=["tipo"]
        verbose_name= 'Tipo'
        verbose_name_plural = "Tipos"
    def __str__(self):
        return self.tipo

class Origen(models.Model):
    pais=models.CharField(max_length=50, null=True, unique=True)
    class Meta:
        ordering=["pais"]
        verbose_name='pais'
        verbose_name_plural='paises'
    def __str__(self):
        return self.pais

class MarcaCerveza(models.Model):
    id = models.AutoField(primary_key=True)
    marca=models.CharField(max_length=50, null= True, unique=True)
    pais=models.ForeignKey(Origen, null=True, blank= False, on_delete=models.CASCADE)
    sitioweb=models.URLField(blank=True, null=True)
    class Meta:
        ordering=["marca"]
        verbose_name= 'marca'
        verbose_name_plural = "marcas"

    def __str__(self):
        return self.marca

class NombreCerveza(models.Model):
    id = models.AutoField(primary_key=True)
    tipo=models.OneToOneField(TipoCerveza, null=True, on_delete=models.CASCADE)
    marca=models.ForeignKey(MarcaCerveza, null=True, on_delete=models.CASCADE)
    nombre=models.CharField(max_length=30, blank=False, null= False)
    color=models.CharField(max_length=30, blank=False, null= False)
    descripcion=models.CharField(max_length=500)
    precio=models.CharField(max_length=4, null=True)
    foto=models.ImageField(upload_to='fotocerv', null=True)

    class Meta:
        ordering=["tipo"]
        verbose_name= 'cerveza'
        verbose_name_plural = "cervezas"

    def __str__(self):
        return "%s %s %s %s %s %s %s" % (self.tipo, self.marca, self.nombre, self.color, self.descripcion, self.precio, self.foto)
