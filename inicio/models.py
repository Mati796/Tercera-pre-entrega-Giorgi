from django.db import models

# Create your models here.

class Pokemon(models.Model):
    nombre = models.CharField(max_length=20)
    pokedex = models.IntegerField()
    
class Entrenador(models.Model):
    nombre = models.CharField(max_length=20)
    edad = models.IntegerField()
    tipo_pokemon = models.CharField(max_length=20)
    
    
class Gimnasio(models.Model):
    nombre = models.CharField(max_length=20)
    ciudad = models.CharField(max_length=20)
    tipo_pokemon = models.CharField(max_length=20)