from django.urls import path
from mensajes import views


app_name = 'mensajes'

urlpatterns = [
    path('ver/', views.ListarMensaje.as_view(), name='mensajes'),
    path('mensajes/crear', views.crear_mensaje, name='crear_mensaje'),
    path('mensajes/exito', views.mensaje_exito, name='mensaje_exito'),
]
