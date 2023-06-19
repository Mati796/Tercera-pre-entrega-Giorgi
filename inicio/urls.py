
from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.inicio),
    path('prueba_template/', views.prueba_template),
    path('crear_pokemon/<str:nombre>/<int:pokedex>/', views.crear_pokemon)
]