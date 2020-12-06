from django.shortcuts import render
from .models import Producto
from django.template import loader

def index(request):
  destacados = Producto.objects.all()[:3]
  context = {
    'Destacados' : destacados,
  }
  return render(request, 'main/index.html',context)

def productos(request):
  productos = Producto.objects.all()
  context = {
    'Productos' : productos,
  }
  return render(request, 'main/productos.html',context)

