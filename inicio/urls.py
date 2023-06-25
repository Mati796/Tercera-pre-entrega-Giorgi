
from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.Inicio, name = 'Inicio'),
    path('about_us/', views.about_us, name = 'about_us'),
    path('pokemon/', views.listar_pokemon, name='listar_pokemon'),
    path('pokemon/crear/', views.crear_pokemon, name='crear_pokemon'),
    path('entrenador/', views.listar_entrenador, name='listar_entrenador'),
    path('entrenador/crear/', views.crear_entrenador, name='crear_entrenador'),
    path('gimnasio/', views.listar_gimnasio, name='listar_gimnasio'),
    path('gimnasio/crear/', views.crear_gimnasio, name='crear_gimnasio'),
    
    
]