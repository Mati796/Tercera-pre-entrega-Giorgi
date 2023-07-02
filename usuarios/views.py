from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth import authenticate, login as django_login
from usuarios.form import MiFormularioDeCreacionDeUsuarios


# Create your views here.


def login(request):
    
    if request.method == 'POST':
        formulario = AuthenticationForm(request, data=request.POST)
        if formulario.is_valid():
           usuario = formulario.cleaned_data['username']
           contrasenia = formulario.cleaned_data['password']
           
           user = authenticate(username=usuario,password=contrasenia)
           
           django_login(request, user)
           return redirect('Inicio:Inicio')
           
           
        else: 
           return render(request, 'usuarios/login.html', {'formulario':formulario})    
    
    formulario = AuthenticationForm()
    return render(request, 'usuarios/login.html', {'formulario':formulario})



def registrarse(request):
    
    if request.method == 'POST':
        formulario = MiFormularioDeCreacionDeUsuarios(request.POST)
        if formulario.is_valid():
            formulario.save()
            return redirect('usuarios:login')
        else:
            return render(request,'usuarios/registrarse.html',{'formulario':formulario})   
    
    
    formulario= MiFormularioDeCreacionDeUsuarios()
    return render(request,'usuarios/registrarse.html',{'formulario':formulario})