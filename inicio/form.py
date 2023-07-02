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



class EntrenadorFormularioBase(forms.Form):
   nombre = forms.CharField(max_length=20)
   edad = forms.IntegerField()
   tipo_pokemon = forms.CharField(max_length=20)
    
class CrearEntrenadorFormulario (EntrenadorFormularioBase):
    ...
    
class ModificarEntrenadorFormulario (EntrenadorFormularioBase):
    ... 

    
class BuscarEntrenadorFormulario (forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
    
    


class GimnasioFormularioBase(forms.Form):
    nombre = forms.CharField(max_length=20)
    ciudad = forms.CharField(max_length=20)
    tipo_pokemon = forms.CharField(max_length=20)
   

class CrearGimnasioFormulario (GimnasioFormularioBase):
    ...
    
    
class ModificarGimnasioFormulario (GimnasioFormularioBase):
    ... 
    
class BuscarGimnasioFormulario (forms.Form):
    nombre = forms.CharField(max_length=20, required=False)
    
    
