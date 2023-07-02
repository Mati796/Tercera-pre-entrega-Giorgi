
from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.Inicio, name = 'Inicio'),
    path('about_us/', views.about_us, name = 'about_us'),
    path('pokemon/', views.listar_pokemon, name='listar_pokemon'),
    path('pokemon/crear/', views.crear_pokemon, name='crear_pokemon'),
    path('pokemon/eliminar/<int:pokemon_id>/', views.eliminar_pokemon, name='eliminar_pokemon'),
    path('pokemon/modificar/<int:pokemon_id>/', views.modificar_pokemon, name='modificar_pokemon'),
    path('entrenador/', views.listar_entrenador, name='listar_entrenador'),
    path('entrenador/crear/', views.crear_entrenador, name='crear_entrenador'),
    path('entrenador/eliminar/<int:entrenador_id>/', views.eliminar_entrenador, name='eliminar_entrenador'),
    path('entrenador/modificar/<int:entrenador_id>/', views.modificar_entrenador, name='modificar_entrenador'),
    path('gimnasio/', views.listar_gimnasio, name='listar_gimnasio'),
    path('gimnasio/crear/', views.crear_gimnasio, name='crear_gimnasio'),
    path('gimnasio/eliminar/<int:gimnasio_id>/', views.eliminar_gimnasio, name='eliminar_gimnasio'),
    path('gimnasio/modificar/<int:gimnasio_id>/', views.modificar_gimnasio, name='modificar_gimnasio'),    
]