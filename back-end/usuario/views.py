from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView
from django.views import View
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
import copy
# Rest
from rest_framework import viewsets
from usuario.serializers import UsuarioSerializer

from . import models
from . import forms


class BasePerfil(View):

    template_name = 'usuario/cadastro_nova.html'

    def setup(self, *args, **kwargs):
        # estou colocando a requisição do métedo 'setup' no método 'super' para eu poder acessar a requisão em 'forms.py'
        super().setup(*args, **kwargs)

        self.usuario = None

        if self.request.user.is_authenticated:

            # self.contexto é um objeto que passa dados para uma classe em 'forms.py'
            self.contexto = {
                'usuarioform': forms.UsuarioForm(
                    data=self.request.POST or None,
                    usuario=self.request.user,
                    instance=self.request.user
                )
            }

            self.renderizar = render(
                self.request, self.template_name, self.contexto
            )

        else:
            self.contexto = {
                'usuarioform': forms.UsuarioForm(data=self.request.POST or None),
            }

        # variaveis com formularios do objeto 'contexto'
        self.usuarioform = self.contexto['usuarioform']

        # se o usuário já estiver logado ele vai ser redirecionado para uma página diferente, que é a att de perfil
        if self.request.user.is_authenticated:
            self.template_name = 'usuario/atualizar.html'

        self.renderizar = render(  # 'self.contexto' será interpretado no documento HTML. EX: {{ userform|crispy }}
            self.request, self.template_name, self.contexto)

    def get(self, *args, **kwargs):
        return self.renderizar

    ######################################################################
    # Tudo isso apenas para renderizar o formulário


# classe para criar e atualizar receitas
class Criar(BasePerfil):
    def post(self, *args, **kwargs):

        # o django forms possui um método chamado 'is_valid()' que executa validações para todos os campos do formuário
        # Se todos os campos do formulário for válido ele retorna True e armazena os dados em 'cleaned_data'
        if not self.usuarioform.is_valid():
            messages.error(
                self.request,
                'VERIFIQUE SE OS CAMPOS ESTÃO PREENCHIDOS CORRETAMENTE!!!'
            )
            return self.renderizar

        # pegando todos os campos do formulário herdado da classe acima e armazenando em variáveis
        username = self.usuarioform.cleaned_data.get('username')
        password = self.usuarioform.cleaned_data.get('password')
        email = self.usuarioform.cleaned_data.get('email')

# ------------------------------------------------------------------------------------------------------
# A partir de agora, usando as variáveis com os dados com formulário

        # checando se o usuário está logado, se estiver logado quer dizer que está atualizando perfil
        if self.request.user.is_authenticated:
            # procurando usuário no model de tipo User recebendo como parâmetro o nome do usuário
            # se não achar o nome do usuário retorna erro 404
            # TODO: usuario não pode alterar o nome (ficar de acordo com o CDU), incluir campo de 'nickname' depois.
            usuario = get_object_or_404(
                User, username=self.request.user.username)

            # atualizando nome
            #usuario.username = username

            # atualizando senha
            if password:
                usuario.set_password(password)

            usuario.email = email
            usuario.save()

        # Usuário não logado (novo)
        else:
            # criando novo usuário
            # 'commit=False' é para deixa pronto para salvar, salvar
            usuario = self.usuarioform.save(commit=False)
            usuario.set_password(password)
            usuario.save()

        if password:
            # 'authenticate' é um método que checa se as crendenciais são válidas
            # se for válido retorna um objeto User
            autentica = authenticate(
                self.request,
                username=usuario,
                password=password,
            )

            if autentica:
                # método login requer como parâmetro uma requisisão e um id user
                login(self.request, user=usuario)

        return redirect('receita:index')


class Login(View):
    def post(self, *args, **kwargs):
        username = self.request.POST.get('username')
        password = self.request.POST.get('password')

        if not username or not password:
            messages.error(
                self.request,
                'USUÁRIO OU SENHA INVALIDOS!!!'
            )
            return redirect('usuario:criar')

        usuario = authenticate(
            self.request, username=username, password=password)

        if not usuario:
            messages.error(
                self.request,
                'USUÁRIO OU SENHA INVALIDOS!!!'
            )
            return redirect('usuario:criar')

        login(self.request, user=usuario)

        messages.success(
            self.request,
            'VOCE FEZ LOGIN!!!'
        )
        return redirect('receita:index')


class Logout(View):
    def get(self, *args, **kwargs):
        logout(self.request)
        messages.info(
            self.request,
            'Vc deslogou'
        )
        return redirect('receita:index')

# TODO: procurar um 'forms.py' para cadastrar receita


class favoritos(View):
    # TODO: adicionar retorno 'render' para tela de favoritos
    pass

# Rest - Serializers

class UsuarioViewSet(viewsets.ModelViewSet):
    serializer_class = UsuarioSerializer
    queryset = models.User.objects.all()
