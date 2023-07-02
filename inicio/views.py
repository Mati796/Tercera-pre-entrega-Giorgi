from django.shortcuts import render, redirect
from django.template import Template
from inicio.models import Pokemon, Entrenador, Gimnasio
from inicio.form import CrearPokemonFormulario, BuscarPokemonFormulario, ModificarPokemonFormulario, CrearEntrenadorFormulario, BuscarEntrenadorFormulario, ModificarEntrenadorFormulario, CrearGimnasioFormulario, BuscarGimnasioFormulario, ModificarGimnasioFormulario
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.urls import reverse_lazy

# Create your views here.

    
def Inicio(request):
    return render (request,'base.html')

def about_us(request):
    return render (request,'about_us.html')




class CrearPokemon(CreateView):
    model = Pokemon
    template_name = 'inicio/CBV/crear_pokemon_CBV.html'
    fields = ['nombre','pokedex','descripcion']
    success_url = reverse_lazy('Inicio:listar_pokemon')
    
    
class ListarPokemon(ListView):
    model = Pokemon
    template_name = 'inicio/CBV/listar_pokemon_CBV.html'
    context_object_name = 'pokemons'


class ModificarPokemon(UpdateView):
    model = Pokemon
    template_name = 'inicio/CBV/modificar_pokemon_CBV.html'
    fields = ['nombre','pokedex', 'descripcion']
    success_url = reverse_lazy('Inicio:listar_pokemon')


class EliminarPokemon(DeleteView):
    model = Pokemon
    template_name = 'inicio/CBV/eliminar_pokemon_CBV.html'
    success_url = reverse_lazy('Inicio:listar_pokemon')


class MostrarPokemon(DetailView):
    model = Pokemon
    template_name = 'inicio/CBV/mostrar_pokemon_CBV.html'
    






def crear_entrenador(request):
    diccionario = {}
    
    if request.method == "POST":
      formulario = CrearEntrenadorFormulario(request.POST)
      if formulario.is_valid():
          info = formulario.cleaned_data
          entrenador = Entrenador(nombre=info['nombre'], edad=info['edad'], tipo_pokemon=info['tipo_pokemon'])
          entrenador.save()
          diccionario['entrenador'] = entrenador
          return render(request, "entrenador.html", diccionario)
      else:
          diccionario['formulario'] = formulario
          return render(request, "entrenador.html", diccionario)
          
    formulario = CrearEntrenadorFormulario()
    diccionario['formulario']= formulario
    return render(request, "crear_entrenador.html", diccionario)

def listar_entrenador(request):
    
    formulario = BuscarEntrenadorFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_de_entrenadores=Entrenador.objects.filter(nombre__icontains=nombre_a_buscar)  
          
      
    formulario = BuscarEntrenadorFormulario()
    return render(request,'listar_entrenador.html', {'formulario2':formulario,'entrenadores':listado_de_entrenadores})

def eliminar_entrenador(request, entrenador_id):
    entrenador = Entrenador.objects.get(id=entrenador_id)
    entrenador.delete()
    
    return redirect('Inicio:listar_entrenador')

def modificar_entrenador(request, entrenador_id):
    entrenador_a_modificar = Entrenador.objects.get(id=entrenador_id)
    
    if request.method == 'POST':
        formulario = ModificarEntrenadorFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            entrenador_a_modificar.nombre = info['nombre']
            entrenador_a_modificar.edad = info['edad']
            entrenador_a_modificar.tipo_pokemon = info['tipo_pokemon']
            entrenador_a_modificar.save()
            return redirect ('Inicio:listar_entrenador')
            
        else: 
            return render(request, 'modificar_entrenador.html',{'formulario':formulario})

    formulario = ModificarEntrenadorFormulario(initial={'nombre':entrenador_a_modificar.nombre, "edad":entrenador_a_modificar.edad,"tipo_pokemon":entrenador_a_modificar.tipo_pokemon})
    return render(request, 'modificar_entrenador.html',{'formulario':formulario})






def crear_gimnasio(request):
    diccionario = {}
    
    if request.method == "POST":
      formulario = CrearGimnasioFormulario(request.POST)
      if formulario.is_valid():
          info = formulario.cleaned_data
          gimnasio = Gimnasio(nombre=info['nombre'], ciudad=info['ciudad'], tipo_pokemon=info["tipo_pokemon"])
          gimnasio.save()
          diccionario['gimnasio'] = gimnasio
          return render(request, "gimnasio.html", diccionario)
      else:
          diccionario['formulario'] = formulario
          return render(request, "gimnasio.html", diccionario)
          
    formulario = CrearGimnasioFormulario()
    diccionario['formulario']= formulario
    return render(request, "crear_gimnasio.html", diccionario)

def listar_gimnasio(request):
    formulario = BuscarGimnasioFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_de_gimnasios=Gimnasio.objects.filter(nombre__icontains=nombre_a_buscar)  
        
    formulario = BuscarGimnasioFormulario()
    return render(request,'listar_gimnasio.html', {'formulario':formulario,'gimnasios':listado_de_gimnasios})


def eliminar_gimnasio(request, gimnasio_id):
    gimnasio = Gimnasio.objects.get(id=gimnasio_id)
    gimnasio.delete()
    
    return redirect('Inicio:listar_gimnasio')
 
def modificar_gimnasio(request, gimnasio_id):
    gimnasio_a_modificar = Gimnasio.objects.get(id=gimnasio_id)
    
    if request.method == 'POST':
        formulario = ModificarGimnasioFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            gimnasio_a_modificar.nombre = info['nombre']
            gimnasio_a_modificar.ciudad = info['ciudad']
            gimnasio_a_modificar.tipo_pokemon = info['tipo_pokemon']
            gimnasio_a_modificar.save()
            return redirect ('Inicio:listar_gimnasio')
            
        else: 
            return render(request, 'modificar_gimnasio.html',{'formulario':formulario})

    formulario = ModificarGimnasioFormulario(initial={'nombre':gimnasio_a_modificar.nombre, "ciudad":gimnasio_a_modificar.ciudad, "tipo_pokemon":gimnasio_a_modificar.tipo_pokemon})
    return render(request, 'modificar_gimnasio.html',{'formulario':formulario})