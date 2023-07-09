from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.

class Mensaje(models.Model):
    usuario = models.CharField(max_length=20) 
    descripcion = RichTextField(null=True)
    
    def __str__(self):
      return f"Usuario: {self.usuario} -Mensaje: {self.descripcion}"
    
    
    