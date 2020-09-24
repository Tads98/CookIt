from django.urls import path
from . import views

urlpatterns = [
    path('', views.ListarReceita.as_view(), name='index')
]
