from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Para upload de imagens
from django.conf.urls.static import static  # Para upload de imagens
from rest_framework.routers import DefaultRouter
from . import views

from receita.views import ReceitaViewSet, IngredienteViewSet, AvaliacaoViewSet  
from usuario.views import UsuarioViewSet  

router = DefaultRouter() 

router.register('receita', ReceitaViewSet, basename = 'receita')
router.register('ingrediente', IngredienteViewSet, basename = 'ingrediente')
router.register('avaliacao', AvaliacaoViewSet, basename = 'avaliacao')

router.register('usuario', UsuarioViewSet, basename = 'usuario')

vue_urls = [
  path('', views.frontend),
  path('another-path/', views.frontend),
]

urlpatterns = [
#   Comentando pra dar espaço ao Vue
#    path('', include('receita.urls')),
#    path('usuario/', include('usuario.urls')),
#    path('admin/', admin.site.urls),
    path('', include(vue_urls)),


    path('api/', include(router.urls) ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Para upload de imagens
