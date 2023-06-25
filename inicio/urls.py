
from django.urls import path
from inicio import views

urlpatterns = [
    path('', views.Inicio, name = 'Inicio'),
    path('about_us/', views.about_us, name = 'about_us'),
    path('crear_pokemon/<str:nombre>/<int:pokedex>/', views.crear_pokemon)
]