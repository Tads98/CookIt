from django.urls import path
from . import views

urlpatterns = [
    path('editar', views.editarPerfil, name='editarPerfil')
]