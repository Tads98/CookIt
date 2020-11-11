from django.urls import path
from . import views

app_name = 'receita'

urlpatterns = [
    path('', views.ListarReceita.as_view(), name='index'),
    path('<slug>', views.DetalheReceita.as_view(), name='receita_completa'),
    path('cadastrar-receita/', views.CadastrarReceita.as_view(),
         name='cadastrar_receita'),
    path('busca/', views.Busca.as_view(), name="busca"),
]
