from django.urls import path
from . import views

urlpatterns = [
    path('editar', views.editarPerfil, name='editarPerfil'),
    path('favoritos', views.favoritos, name='favoritos'),
    # TODO: lembrar de deixar as duas telas de cadastro em apenas uma URL
    path('cadastrar-editar_receita', views.CadastrarEditar_Receita,
         name='cadastrareditarreceita'),
]
