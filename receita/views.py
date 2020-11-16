from receita.models import Ingrediente, Receita
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone

from . import models
from . import forms


class ListarReceita(ListView):
    model = models.Receita
    template_name = 'receita/index.html'
    context_object_name = 'receitas'
    paginate_by = 12
    queryset = models.Receita.objects.order_by('-data_publicacao')


class Busca(ListarReceita):
    def get_queryset(self, *args, **kwargs):
        print("Busca foi acionada!")
        termo = self.request.GET.get('termo') or self.request.session['termo']
        sabor = self.request.GET.get('sabor')
        print(f'Nome da receita: {termo}')
        print(f'Sabor: {sabor}')
        qs = super().get_queryset(*args, **kwargs)

        if not termo and not sabor:
            print(qs.query)
            return qs

        self.request.session['termo'] = termo

        if termo:
            qs = qs.filter(
                Q(nome_receita__icontains=termo)
            )

        if sabor:
            qs = qs.filter(
                Q(sabor_receita=sabor)
            )

        if termo and sabor:
            qs = qs.filter(
                Q(nome_receita__icontains=termo) &
                Q(sabor_receita=sabor)
            )

        self.request.session.save()
        print(qs)

        return qs


class DetalheReceita(DetailView):
    model = models.Receita
    template_name = 'receita/receita-completa.html'
    context_object_name = 'ingrediente'
    slug_url_kwargs = 'slug'


class BaseCadastrar(View):

    template_name = 'receita/editar_receita.html'

    def setup(self, *args, **kwargs):
        # estou colocando a requisição do métedo 'setup' no método 'super' para eu poder acessar a requisão em 'forms.py'
        super().setup(*args, **kwargs)

        # checando se o usuário está autenticado
        if self.request.user.is_authenticated:

            self.nome = models.Receita.objects.filter().first()

            self.contexto = {
                'receitaform': forms.ReceitaForm(
                    files=self.request.FILES,
                    data=self.request.POST or None,
                    receita=self.request.POST,
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

        self.renderizar = render(  # 'self.contexto' será interpretado no documento HTML. EX: {{ receitaform|crispy }}
            self.request, self.template_name, self.contexto)

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


##################################################################################

        # checando se o usuário está logado, se estiver logado quer dizer que está atualizando a receita
        if self.request.user.is_authenticated:
            ingrediente = self.ingredienteform.save(commit=False)
            ingrediente.receita = self.receitaform.save()
            ingrediente.save()

        else:
            # cadastrando nova receita
            # 'commit=False'cria um objeto com id mas sem salvar ainda na base de dados
            ingrediente = self.ingredienteform.save(commit=False)
            ingrediente.receita = self.receitaform.save()
            ingrediente.save()

        return redirect('receita:index')
