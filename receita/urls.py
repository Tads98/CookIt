from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListarReceita.as_view(), name='index'),
    path('<slug>', views.DetalheReceita.as_view(), name='receita_completa'),
]
