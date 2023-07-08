from django.db import models
from ckeditor.fields import RichTextField

# Create your models here.

class Pokemon(models.Model):
    nombre = models.CharField(max_length=20)
    tipo = models.CharField(max_length=20)
    evolucion = models.CharField(max_length=20)
    fecha_creacion = models.DateField()
    descripcion = RichTextField(null=True)
    icono = models.ImageField(upload_to='iconos',null=True,blank=True)
    
    
    def __str__(self):
        return f"Pokemon: {self.nombre} -Tipo: {self.tipo} - Evoluciona en: {self.evolucion} - Fue creado con fecha: {self.fecha_creacion}"
    
    
class Entrenador(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    tipo_pokemon = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Entrenador: {self.nombre}  -  Edad: {self.edad}  -  Tipo de pokemons: {self.tipo_pokemon}"
  
    
    
class Gimnasio(models.Model):
    nombre = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    tipo_pokemon = models.CharField(max_length=20)
    
    def __str__(self):
        return f"Gimnasio: {self.nombre}  -  Ciudad: {self.ciudad}  -  Tipo de pokemons: {self.tipo_pokemon}"