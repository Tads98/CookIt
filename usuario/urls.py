from django.urls import path
from . import views

app_name = 'usuario'

urlpatterns = [
    path('', views.Atualizar.as_view(), name='atualizar'),
    path('cadastrar', views.Cadastrar.as_view(), name='cadastrar'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('favoritos', views.favoritos, name='favoritos'),
    # TODO: lembrar de deixar as duas telas de cadastro em apenas uma URL
    path('cadastrar-editar_receita', views.CadastrarEditar_Receita,
         name='cadastrareditarreceita'),
]
