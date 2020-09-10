from django.urls import path
from . import views

urlpatterns = [
    path('editar', views.editarPerfil, name='editarPerfil'),
    path('favoritos', views.favoritos, name='favoritos'),
    path('cadastro1', views.cadastro_usuario1, name='favoritos'),
    # TODO: lembrar de deixar as duas telas de cadastro em apenas uma URL
    path('cadastro2', views.cadastro_usuario2, name='favoritos'),
    path('cadastrar-editar_receita', views.CadastrarEditar_Receita,
         name='cadastrareditarreceita'),
]
