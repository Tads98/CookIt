from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . import models

#TODO: paginate_by
class ListarReceita(ListView):
    model = models.Receita
    template_name = 'receita/index.html'
    context_object_name = 'receitas'

#TODO: DetailView

