from django.db import models

def nombre_imagen_producto(instance,filename):
    return instance.nombre.lower() + ".png"

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)

    class Meta:
        ordering = ['nombre']
    
    def _str_(self):
        return '%s' % (self.nombre)



# Create your models here.
class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to=nombre_imagen_producto,blank=True,null=True)
    precio = models.FloatField(blank=True,null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        ordering = ['nombre']
    def __str__(self):
        return '%s' % (self.nombre)

