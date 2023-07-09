from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from mensajes.forms import MiFormularioDeCreacionDeMensaje
from django.contrib.auth.models import User
from mensajes.models import Mensaje
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.

class ListarMensaje(LoginRequiredMixin, ListView):
    model = Mensaje
    template_name = 'mensajes/listar_mensajes.html'
    context_object_name = 'mensajes'



@login_required
def crear_mensaje(request):
    diccionario = {}

    if request.method == "POST":
      formulario = MiFormularioDeCreacionDeMensaje(request.POST)
      if formulario.is_valid():
          info = formulario.cleaned_data
          info['usuario'] = request.user.username
          mensaje = Mensaje(usuario=info['usuario'], descripcion = info['descripcion'])
          mensaje.save()
          diccionario['mensaje'] = mensaje
          return render(request, "mensajes/mensaje_exito.html", diccionario)
      else:
          diccionario['formulario'] = formulario
          return render(request, "mensajes/mensaje_exito.html", diccionario)
          
    formulario = MiFormularioDeCreacionDeMensaje()
    diccionario['formulario']= formulario
    return render(request, "mensajes/crear_mensaje.html", diccionario)


@login_required
def mensaje_exito(request):
    return render(request,'mensajes/mensaje_exito.html')