from django.http import HttpResponse


def inicio(request):
    return HttpResponse ("<h1> Hola, soy Mati<h1>")