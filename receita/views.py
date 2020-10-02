from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from . import models


class ListarReceita(ListView):
    model = models.Receita
    template_name = 'receita/index.html'
    context_object_name = 'receitas'
    paginate_by = 12


class DetalheReceita(DetailView):
    model = models.Receita
    template_name  = 'receita/receita-completa.html'
    context_object_name = 'ingrediente'
    slug_url_kwargs = 'slug' 

