from django.http import HttpResponse
from django.template import Template, Context , loader


def inicio(request):
    # archivo = open(r"C:\Users\ET471NQ\OneDrive - EY\Desktop\Mi_django\Templates\inicio.html","r")
    
    template = loader.get_template("inicio.html")
    
    # archivo.close()
    
    diccionario = {
        "mensaje":"Hola, soy Magi_One"
        }
    
    # contexto = Context(diccionario)
        
    renderizar_template = template.render(diccionario)

    return HttpResponse(renderizar_template)



