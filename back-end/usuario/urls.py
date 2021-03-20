from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

#app_name = 'usuario'

#router = DefaultRouter() 

#router.register('usuario', views.UsuarioViewSet, basename = 'usuario')

urlpatterns = [
    path('', views.Criar.as_view(), name='criar'),
    path('login/', views.Login.as_view(), name='login'),
    path('logout/', views.Logout.as_view(), name='logout'),
    path('favoritos', views.favoritos, name='favoritos'),

    #path('api/', include(router.urls) ),
]
