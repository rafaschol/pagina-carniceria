from django.shortcuts import render
from .models import *
from django.template import loader

def index(request):
  destacados = Producto.objects.all()[:3]
  context = {
    'destacados': destacados,
  }
  return render(request, 'main/index.html', context)

def productos(request):
  productos = {}
  for categoria in Categoria.objects.all():
    productos[categoria] = categoria.producto_set.all()

  context = {
    'productos': productos,
  }
  return render(request, 'main/productos.html', context)