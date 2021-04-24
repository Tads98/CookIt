from django.views.generic import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView
from django.views import View
from django.shortcuts import redirect
from django.urls import reverse
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages
from django.db.models import Q
from .models import Receita
from . import models
from .forms import ReceitaForm
from django_filters.rest_framework import FilterSet
import django_filters
# Rest
from rest_framework import viewsets, filters
from receita.serializers import ( ReceitaSerializer, IngredienteSerializer, 
                                AvaliacaoSerializer, UserSerializer,
                                PostReceitaSerializer )

class ListarReceita(ListView):
    model = models.Receita
    template_name = 'receita/index.html'
    context_object_name = 'receitas'
    paginate_by = 12
    ordering = ['-data_publicacao']


class Busca(ListarReceita):
    def get_queryset(self, *args, **kwargs):
        termo = self.request.GET.get(
            'termo') or self.request.session.get('termo', None)
        sabor = self.request.GET.getlist(
            'sabor') or self.request.session.get('sabor', None)
        dificuldade = self.request.GET.get(
            'dificuldade') or self.request.session.get('dificuldade', None)
        porcoes = self.request.GET.get(
            'porcoes') or self.request.session.get('porcoes', None)
        ingredientes = self.request.GET.getlist(
            'ingredientes') or self.request.session.get('ingredientes', None)

        self.request.session['busca']['termo'] = termo
        self.request.session['busca']['sabor'] = sabor
        self.request.session['busca']['dificuldade'] = dificuldade
        self.request.session['busca']['porcoes'] = porcoes
        self.request.session['busca']['ingredientes'] = ingredientes

        qs = super().get_queryset(*args, **kwargs)
        # TODO: fazer com assentos
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
        # TODO: clear deslogando usuario, concertar
        self.request.session.clear()
        return redirect('receita:index')


class DetalheReceita(DetailView):
    model = models.Receita
    template_name = 'receita/receita-completa.html'
    context_object_name = 'ingredientes'
    slug_url_kwargs = 'slug'

class CadastrarReceita(LoginRequiredMixin, CreateView):
    # TODO: dar um jeito enviar uma mensagem de aviso para o usuário via 'messages'
    login_url = 'usuario:criar'
    template_name = 'receita/teste.html'
    model = models.Receita
    form_class = ReceitaForm

    def get_success_url(self):
        return reverse('receita:index')

    def form_valid(self, form_class):
        receita = form_class.save(commit=False)
        receita.dono_receita = self.request.user
        return super(CadastrarReceita, self).form_valid(form_class)

# Rest - Serializers

class ReceitaFilter(FilterSet):
    ingredientes_not = django_filters.BaseInFilter(field_name='ingredientes__nome_ingrediente', lookup_expr='in', exclude=True)
    
    class Meta:
        model = Receita
        fields = {
            'nome_receita': ['icontains'],
            'sabor_receita': ['in'],
            'dificuldade': ['exact'],
            'categoria': ['in'],
            'ingredientes__nome_ingrediente': ['in'],
        }

class ReceitaViewSet(viewsets.ModelViewSet):
    queryset = models.Receita.objects.all()
    serializer_class = ReceitaSerializer
    filterset_class = ReceitaFilter

class PostReceitaViewSet(viewsets.ModelViewSet):
    serializer_class = PostReceitaSerializer
    queryset = models.Receita.objects.all()

class IngredienteViewSet(viewsets.ModelViewSet):
    serializer_class = IngredienteSerializer
    queryset = models.Ingrediente.objects.all()

class AvaliacaoViewSet(viewsets.ModelViewSet):
    serializer_class = AvaliacaoSerializer
    queryset = models.Avaliacao.objects.all()

class UserViewSet(viewsets.ModelViewSet):
    serializer_class = UserSerializer
    queryset = models.User.objects.all()


