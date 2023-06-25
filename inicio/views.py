from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import Template, Context , loader
from inicio.models import Pokemon




def crear_pokemon(request, nombre, pokedex):
    
    pokemon = Pokemon(nombre=nombre, pokedex=pokedex)
    pokemon.save()
    diccionario = {
        "nombre":nombre,
        "pokedex":pokedex,
        }
    
    return render(request, "crear_pokemon.html", diccionario)
 
    
    
def Inicio(request):
    return render (request,'base.html')

def about_us(request):
    return render (request,'about_us.html')