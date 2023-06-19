from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from django.template import Template, Context , loader
from inicio.models import Pokemon


def inicio(request):
    # archivo = open(r"C:\Users\ET471NQ\OneDrive - EY\Desktop\Mi_django\Templates\inicio.html","r")
    
    # template = loader.get_template("inicio.html")
    
    # archivo.close()
    
    diccionario = {
        "mensaje":"Hola, soy Magi_One"
        }
    
    return render(request, "inicio.html", diccionario )
    
    # contexto = Context(diccionario)
        
    # renderizar_template = template.render(diccionario)

    # return HttpResponse(renderizar_template)


def crear_pokemon(request, nombre, pokedex):
    # template = loader.get_template("crear_pokemon.html")
    
    pokemon = Pokemon(nombre=nombre, pokedex=pokedex)
    pokemon.save()
    diccionario = {
        "nombre":nombre,
        "pokedex":pokedex,
        }
    
    return render(request, "crear_pokemon.html", diccionario)
    # renderizar_template = template.render(diccionario)

    # return HttpResponse(renderizar_template)
    
    
    
def prueba_template(request):
    return render (request,"index.html")