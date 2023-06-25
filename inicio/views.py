from django.shortcuts import render
from django.template import Template
from inicio.models import Pokemon, Entrenador, Gimnasio
from inicio.form import CrearPokemonFormulario, BuscarPokemonFormulario, CrearEntrenadorFormulario, BuscarEntrenadorFormulario, CrearGimnasioFormulario, BuscarGimnasioFormulario

# Create your views here.

    
def Inicio(request):
    return render (request,'base.html')

def about_us(request):
    return render (request,'about_us.html')


def crear_pokemon(request):
    diccionario = {}
    
    if request.method == "POST":
      formulario = CrearPokemonFormulario(request.POST)
      if formulario.is_valid():
          info = formulario.cleaned_data
          pokemon = Pokemon(nombre=info['nombre'], pokedex=info['pokedex'])
          pokemon.save()
          diccionario['pokemon'] = pokemon
          return render(request, "pokemon.html", diccionario)
      else:
          diccionario['formulario'] = formulario
          return render(request, "pokemon.html", diccionario)
          
    formulario = CrearPokemonFormulario()
    diccionario['formulario']= formulario
    return render(request, "crear_pokemon.html", diccionario)

def listar_pokemon(request):
    formulario = BuscarPokemonFormulario(request.GET)
    if formulario.is_valid():
        nombre_a_buscar = formulario.cleaned_data['nombre']
        listado_de_pokemons=Pokemon.objects.filter(nombre__icontains=nombre_a_buscar)  
          
      
    formulario = BuscarPokemonFormulario()
    return render(request,'listar_pokemon.html', {'formulario':formulario,'pokemons':listado_de_pokemons})


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
