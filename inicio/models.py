from django.db import models

# Create your models here.

class Pokemon(models.Model):
    nombre = models.CharField(max_length=20)
    pokedex = models.IntegerField()
    descripcion = models.TextField(null=True)
    
    def __str__(self):
        return f"Pokemon: {self.nombre} - Numero de pokedex: {self.pokedex}"
    
    
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