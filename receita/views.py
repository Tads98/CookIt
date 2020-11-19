from django.db.models.query import QuerySet
from django.views.generic.base import TemplateResponseMixin
from django.shortcuts import render, get_object_or_404, redirect
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
        print("Busca foi acionada!")
        termo = self.request.GET.getlist(
            'termo') or self.request.session['termo']
        sabor = self.request.GET.get('sabor') or self.request.session['sabor']
        dificuldade = self.request.GET.get(
            'dificuldade') or self.request.session['dificuldade']
        print(f'Nome da receita: {termo}')

        print(f'Sabor: {sabor}')
        print(f'Dificuldade: {dificuldade}')
        qs = super().get_queryset(*args, **kwargs)

        self.request.session['termo'] = termo
        self.request.session['sabor'] = sabor
        self.request.session['dificuldade'] = dificuldade

        if termo:
            qs = qs.filter(
                Q(nome_receita__icontains=termo)
            )

        if sabor:
            qs = qs.filter(
                Q(sabor_receita__icontains=sabor)
            )

        if dificuldade:
            qs = qs.filter(
                Q(dificuldade=dificuldade)
            )

        print(qs)
        self.request.session.save()

        return qs


class Limpar(View):
    def get(self, *args, **kwargs):

        if self.request.session.has_key('termo'):
            print("SESSÃO TERMO LIMPA!!!!!")
            # TODO: procurar uma solução mais sofisticada onde o método flush ou clear
            # consiga limpar uma chave específica e não exclui-la
            self.request.session['termo'] = None

        if self.request.session.has_key('sabor'):
            print("SESSÃO SABOR LIMPA!!!!!")
            self.request.session['sabor'] = None

        if self.request.session.has_key('dificuldade'):
            print("SESSÃO DIFICULDADE LIMPA!!!!!")
            self.request.session['dificuldade'] = None

        return redirect('receita:index')


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
