from django.shortcuts import render
from .models import *
from django.template import loader
from carniceria.settings import EMAIL_HOST_USER
from . import forms
from django.core.mail import send_mail
from django.contrib import messages

def index(request):
  form = forms.EnvioMail()
  if request.method == 'POST':
    form = forms.EnvioMail(request.POST)
    if form.is_valid():
      nombre = form.cleaned_data['nombre']
      apellido = form.cleaned_data['apellido']
      email = form.cleaned_data['email']
      mensaje = form.cleaned_data['mensaje']
      try:
        send_mail("Mensaje recibido en laonce.com.uy", "Ha recibido el mensaje de " + nombre + ", " + apellido + ".\n" + mensaje, EMAIL_HOST_USER, ['gonga.silva1999@gmail.com'])
        messages.success(request, ' Se ha enviado correctamente el mensaje. ') 
      except:
        messages.error(request,' Ha ocurrido un error, verifique los datos,')
    else:
      messages.error(request, 'Ha ocurrido un error, verifique los datos ingresados')
  destacados = Producto.objects.all()[:8]
  context = {
    'destacados': destacados,
    'form' : form,
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