from django import forms


class PokemonFormularioBase(forms.Form):
    nombre = forms.CharField(max_length=20)
    pokedex = forms.IntegerField()

class CrearPokemonFormulario (PokemonFormularioBase):
   ...
    
    
class ModificarPokemonFormulario (PokemonFormularioBase):
    ...


class BuscarPokemonFormulario (forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
    

    
class CrearEntrenadorFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    edad = forms.IntegerField()
    tipo_pokemon = forms.CharField(max_length=20)
    
class BuscarEntrenadorFormulario (forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
    
class CrearGimnasioFormulario (forms.Form):
    nombre = forms.CharField(max_length=20)
    ciudad = forms.CharField(max_length=20)
    tipo_pokemon = forms.CharField(max_length=20)
    
class BuscarGimnasioFormulario (forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
    
