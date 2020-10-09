from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import copy

from . import models
from . import forms


class ListarReceita(ListView):
    model = models.Receita
    template_name = 'receita/index.html'
    context_object_name = 'receitas'
    paginate_by = 12
    queryset = models.Receita.objects.order_by('-data_publicacao')

class DetalheReceita(DetailView):
    model = models.Receita
    template_name  = 'receita/receita-completa.html'
    context_object_name = 'ingrediente'
    slug_url_kwargs = 'slug' 

class BaseCadastrar(View):
    template_name = 'receita/editar_receita.html'

    def post(self, request, *args, **kwargs):

        receita_form = forms.ReceitaForm(data=request.POST)
        receita = receita_form.save()
        receita.data_publicacao = timezone.now()
        receita.save()

        return HttpResponseRedirect(reverse('receita:index'))
    
    def get(self, request, *args, **kwargs):
        receita_form = forms.ReceitaForm()
        
        return render(request, 'receita/editar_receita.html',{'receita_form':receita_form})