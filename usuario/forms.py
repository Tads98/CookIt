from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from . import models


class UsuarioForm(forms.ModelForm):
    # criando um novo campo no formulário
    password = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Senha'
    )
    # criando um novo campo no formulário
    password2 = forms.CharField(
        required=False,
        widget=forms.PasswordInput(),
        label='Confirmação senha'
    )

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: entender da onde vem esse 'self.usuario'
        self.usuario = usuario

    class Meta:
        model = User
        # campos que serão exibidos para prencher no formulário
        # alguns campos são herdados de forms, outros podem ser criados como 'password' e 'password2'
        fields = ('first_name', 'last_name', 'username',
                  'password', 'password2', 'email')