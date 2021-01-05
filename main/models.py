from django.db import models

def nombre_imagen_producto(instance, filename):
    return instance.nombre.lower() + ".png"

def nombre_imagen_producto_activo(instance, filename):
    return instance.nombre.lower() + "_activo.png"

class Categoria(models.Model):
    nombre = models.CharField(max_length=40)
    icono = models.ImageField(upload_to=nombre_imagen_producto, blank=True, null=True)
    icono_activo = models.ImageField(upload_to=nombre_imagen_producto_activo, blank=True, null=True)
    indice = models.IntegerField(blank=True,null=True)

    class Meta:
        ordering = ['indice']
    
    def __str__(self):
        return self.nombre

    def texto_etiqueta(self):
        return self.nombre.replace(' ', '_').lower()


class Producto(models.Model):
    nombre = models.CharField(max_length=40)
    imagen = models.ImageField(upload_to=nombre_imagen_producto,blank=True,null=True)
    precio = models.FloatField(blank=True,null=True)
    categoria = models.ForeignKey(Categoria,on_delete=models.SET_NULL,null=True,blank=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre