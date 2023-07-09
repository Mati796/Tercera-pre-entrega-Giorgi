from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User
from django.db import models
from ckeditor.fields import RichTextFormField
    
    
    
class MiFormularioDeCreacionDeMensaje(forms.Form):
    usuario = User.username
    descripcion = RichTextFormField()
    
    
  