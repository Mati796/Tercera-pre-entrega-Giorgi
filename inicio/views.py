from django.shortcuts import render, redirect
from django.template import Template
from inicio.models import Pokemon, Entrenador, Gimnasio
from inicio.form import CrearPokemonFormulario, BuscarPokemonFormulario, ModificarPokemonFormulario, CrearEntrenadorFormulario, BuscarEntrenadorFormulario, ModificarEntrenadorFormulario, CrearGimnasioFormulario, BuscarGimnasioFormulario, ModificarGimnasioFormulario

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

def eliminar_pokemon(request, pokemon_id):
    pokemon = Pokemon.objects.get(id=pokemon_id)
    pokemon.delete()
    
    return redirect('listar_pokemon')

def modificar_pokemon(request, pokemon_id):
    pokemon_a_modificar = Pokemon.objects.get(id=pokemon_id)
    
    if request.method == 'POST':
        formulario = ModificarPokemonFormulario(request.POST)
        if formulario.is_valid():
            info = formulario.cleaned_data
            pokemon_a_modificar.nombre = info['nombre']
            pokemon_a_modificar.pokedex = info['pokedex']
            pokemon_a_modificar.save()
            return redirect ('listar_pokemon')
            
        else: 
            return render(request, 'modificar_pokemon.html',{'formulario':formulario})

    formulario = ModificarPokemonFormulario(initial={'nombre':pokemon_a_modificar.nombre, "pokedex":pokemon_a_modificar.pokedex})
    return render(request, 'modificar_pokemon.html',{'formulario':formulario})




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
    
    return redirect('listar_entrenador')

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
            return redirect ('listar_entrenador')
            
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
    
    return redirect('listar_gimnasio')
 
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
            return redirect ('listar_gimnasio')
            
        else: 
            return render(request, 'modificar_gimnasio.html',{'formulario':formulario})

    formulario = ModificarGimnasioFormulario(initial={'nombre':gimnasio_a_modificar.nombre, "ciudad":gimnasio_a_modificar.ciudad, "tipo_pokemon":gimnasio_a_modificar.tipo_pokemon})
    return render(request, 'modificar_gimnasio.html',{'formulario':formulario})