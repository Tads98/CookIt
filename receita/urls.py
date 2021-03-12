from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'receita'

router = DefaultRouter() 

router.register('receita', views.ReceitaViewSet, basename = 'receita')
router.register('ingrediente', views.IngredienteViewSet, basename = 'ingrediente')
router.register('avaliacao', views.AvaliacaoViewSet, basename = 'avaliacao')

urlpatterns = [
    path('', views.ListarReceita.as_view(), name='index'),
    path('<slug>', views.DetalheReceita.as_view(), name='receita_completa'),
    path('cadastrar-receita/', views.CadastrarReceita.as_view(),
         name='cadastrar_receita'),
    path('busca/', views.Busca.as_view(), name='busca'),
    path('limpar/', views.Limpar.as_view(), name='limpar'),

    path('api/', include(router.urls) ),
]
