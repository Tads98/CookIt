from os import error
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from . import models


class UsuarioForm(forms.ModelForm):
    # criando um novo campo no formulário

    username = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-group form-contro rounded-pill',
            'placeholder': 'Nome de Usuário',
        }
    ), label='')

    email = forms.CharField(widget=forms.EmailInput(
        attrs={
            'class': 'form-group form-control rounded-pill',
            'placeholder': 'Email',
        }
    ), label='')

    password = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-group form-control rounded-pill',
            'placeholder': 'Senha',
        }
    ),  required=False,
        label=''
    )
    # criando um novo campo no formulário
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class': 'form-group form-control rounded-pill',
            'placeholder': 'Confirmar Senha',
        }
    ),  required=False,
        label=''
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # 'self.usuario' está armazendo um parâmento da função acima
        self.usuario = usuario

    class Meta:
        model = User
        # campos que serão exibidos para prencher no formulário
        # alguns campos são herdados de forms, outros podem ser criados como 'password' e 'password2'
        fields = ('username', 'email',
                  'password', 'password2')


###############################################################################

    # FAZENDO CHECAGEM DE DADOS CADASTRAIS

    def clean(self, *args, **kwargs):
        data = self.data

        # Se todos os campos do formulário for válido ele retorna True e armazena os dados em 'cleaned_data'
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        usuario_data = cleaned.get('username')
        email_data = cleaned.get('email')
        password_data = cleaned.get('password')
        password2_data = cleaned.get('password2')

        usuario_db = User.objects.filter(username=usuario_data).first()
        print(f'Usuario depois da consulta: {usuario_db}')

        email_db = User.objects.filter(email=email_data).first()
        print(f'Email depois da consulta: {email_db}')

        print(' ')

        error_msg_user_exists = 'Usuário já existe'
        error_msg_email_exists = 'E-mail já existe'
        error_msg_password_match = 'As duas senhas não conferem'
        error_msg_password_short = 'Sua senha precisa de pelo menos 6 caracteres'
        error_msg_required_field = 'Este campo é obrigatório'

        # usuários logados atualização
        if self.usuario:
            if not usuario_db:
                validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                if email_data != email_db.email:
                    validation_error_msgs['email'] = error_msg_email_exists

            if password_data:
                if password_data != password2_data:
                    validation_error_msgs['password'] = error_msg_password_match
                    validation_error_msgs['password2'] = error_msg_password_match

                if len(password_data) < 6:
                    validation_error_msgs['password'] = error_msg_password_short

        # usuários não logados cadastro
        else:
            if usuario_db:
                validation_error_msgs['username'] = error_msg_user_exists

            if email_db:
                validation_error_msgs['email'] = error_msg_email_exists

            if not password_data:
                validation_error_msgs['password'] = error_msg_required_field

            if not password2_data:
                validation_error_msgs['password2'] = error_msg_required_field

            if password_data != password2_data:
                validation_error_msgs['password'] = error_msg_password_match
                validation_error_msgs['password2'] = error_msg_password_match

            if len(password_data) < 6:
                validation_error_msgs['password'] = error_msg_password_short

        if validation_error_msgs:
            raise(
                forms.ValidationError(validation_error_msgs)
            )
