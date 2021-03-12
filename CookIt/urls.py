"""CookIt URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # Para upload de imagens
from django.conf.urls.static import static  # Para upload de imagens
from rest_framework.routers import DefaultRouter

from receita.views import ReceitaViewSet, IngredienteViewSet, AvaliacaoViewSet  
from usuario.views import UsuarioViewSet  

router = DefaultRouter() 

router.register('receita', ReceitaViewSet, basename = 'receita')
router.register('ingrediente', IngredienteViewSet, basename = 'ingrediente')
router.register('avaliacao', AvaliacaoViewSet, basename = 'avaliacao')

router.register('usuario', UsuarioViewSet, basename = 'usuario')

urlpatterns = [
    path('', include('receita.urls')),
    path('usuario/', include('usuario.urls')),
    path('admin/', admin.site.urls),

    path('api/', include(router.urls) ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # Para upload de imagens
