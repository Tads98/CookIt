from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.Criar.as_view(), name='criar'),
    path('editar', views.editarPerfil, name='editarPerfil'),
    path('favoritos', views.favoritos, name='favoritos'),
    # TODO: lembrar de deixar as duas telas de cadastro em apenas uma URL
    path('cadastrar-editar_receita', views.CadastrarEditar_Receita,
         name='cadastrareditarreceita'),
]
