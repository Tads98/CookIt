from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.contrib import messages
from django.db.models import Q
from . import models
from . import forms


class ListarReceita(ListView):
    model = models.Receita
    template_name = 'receita/index.html'
    context_object_name = 'receitas'
    paginate_by = 12
    ordering = ['-data_publicacao']


class Busca(ListarReceita):
    def get_queryset(self, *args, **kwargs):
        termo = self.request.GET.get('termo') or self.request.session.get('termo', None)
        sabor = self.request.GET.getlist('sabor') or self.request.session.get('sabor', None)
        dificuldade = self.request.GET.get('dificuldade') or self.request.session.get('dificuldade', None)
        porcoes = self.request.GET.get('porcoes') or self.request.session.get('porcoes', None)
        ingredientes = self.request.GET.getlist('ingredientes') or self.request.session.get('ingredientes', None)
         

        self.request.session['busca']['termo'] = termo
        self.request.session['busca']['sabor'] = sabor
        self.request.session['busca']['dificuldade'] = dificuldade
        self.request.session['busca']['porcoes'] = porcoes
        self.request.session['busca']['ingredientes'] = ingredientes

        qs = super().get_queryset(*args, **kwargs)
        #TODO: fazer com assentos
        if termo:
            qs = qs.filter(
                Q(nome_receita__icontains=termo)
            )
        if sabor:
            qs = qs.filter(
                Q(sabor_receita__in=sabor)
            )

        if dificuldade:
            qs = qs.filter(
                Q(dificuldade=dificuldade)
            )

        if porcoes:
            qs = qs.filter(
                Q(porcoes__lte=porcoes)
            )

        if ingredientes:
            qs = qs.filter(
                Q(ingrediente__nome_ingrediente__iregex=r'(' +
                  '|'.join(ingredientes) + ')')
            )

        self.request.session.save()
        return qs

class Limpar(View):
    def get(self, *args, **kwargs):
        #TODO: clear deslogando usuario, concertar 
        self.request.session.clear()
        return redirect('receita:index')

class DetalheReceita(DetailView):
    model = models.Receita
    template_name = 'receita/receita-completa.html'
    context_object_name = 'ingredientes'
    slug_url_kwargs = 'slug'


class BaseCadastrar(View):
    template_name = 'receita/editar_receita.html'

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)

        if self.request.user.is_authenticated:

            self.contexto = {
                'receitaform': forms.ReceitaForm(
                    files=self.request.FILES,
                    data=self.request.POST or None,
                ),
                'ingredienteform': forms.IngredienteForm(
                    data=self.request.POST
                )
            }

            self.renderizar = render(
                self.request, self.template_name, self.contexto
            )

        else:
            self.contexto = {
                'receitaform': forms.ReceitaForm(data=self.request.POST or None),
                'ingredienteform': forms.IngredienteForm(data=self.request.POST or None),
            }

        self.receitaform = self.contexto['receitaform']
        self.ingredienteform = self.contexto['ingredienteform']

        if self.request.user.is_authenticated:
            self.template_name = 'receita/att_receita.html'

        self.renderizar = render(self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar


class CadastrarReceita(BaseCadastrar):
    def post(self, *args, **kwargs):

        if not self.receitaform.is_valid():
            messages.error(
                self.request,
                'VERIFIQUE SE OS CAMPOS ESTÃO PREENCHIDOS CORRETAMENTE!!!'
            )
            return self.renderizar

        nome_receita = self.receitaform.cleaned_data.get('nome_receita')
        modo_preparo = self.receitaform.cleaned_data.get('modo_preparo')
        tempo_preparo = self.receitaform.cleaned_data.get('tempo_preparo')
        porcoes = self.receitaform.cleaned_data.get('porcoes')
        tempo_unidade_medida = self.receitaform.cleaned_data.get(
            'tempo_unidade_medida')
        foto = self.receitaform.cleaned_data.get('fotos')
        dificuldade = self.receitaform.cleaned_data.get('dificuldade')
        sabor_receita = self.receitaform.cleaned_data.get('sabor_receita')

        nome_ingrediente = self.ingredienteform.cleaned_data.get(
            'nome_ingrediente')
        unidadeMedida = self.ingredienteform.cleaned_data.get('unidadeMedida')
        quantidade = self.ingredienteform.cleaned_data.get('quantidade')


        if self.request.user.is_authenticated:
            ingrediente = self.ingredienteform.save(commit=False)
            ingrediente.receita = self.receitaform.save(commit=False)
            ingrediente.receita.dono_receita = self.request.user
            ingrediente.receita.save()
            ingrediente.save()

        else:
    
            ingrediente = self.ingredienteform.save(commit=False)
            ingrediente.receita = self.receitaform.save(commit=False)
            ingrediente.receita.dono_receita = self.request.user
            ingrediente.receita.save()
            ingrediente.save()

        return redirect('receita:index')