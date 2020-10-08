from os import error
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from . import models

class ReceitaForm(forms.ModelForm):

    nome_receita = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-group form-contro rounded-pill',
            'placeholder': 'Nome da Receita',
        }
    ), label='')

    modo_preparo = forms.IntegerField(widget=forms.Textarea(
        attrs={
            'class': 'form-group form-contro rounded-pill',
            'placeholder': 'Modo de Preparo',
        }
    ), label='')

    tempo_preparo = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class': 'form-group form-contro rounded-pill',
            'placeholder': 'Tempo de Preparo',
        }
    ), label='')

    tempo_unidade_medida = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-group form-contro rounded-pill',
            'placeholder': 'Unidade de Tempo',
        }
    ), label='')

    dono_receita = = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-group form-contro rounded-pill',
            'placeholder': 'Chef',
        }
    ), label='')

    fotos = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class': 'form-group form-contro rounded-pill',
            'placeholder': 'Fotos',
        }
    ), label='')

    dificuldade = forms.ChoiceField(widget=forms.Select(
        attrs={
            'class': 'form-group form-contro rounded-pill',
            'placeholder': 'Dificuldade',
        }
    ), label='')

    data_publicacao = forms.DateTimeField(widget=forms.DateTimeInput(
        attrs={
            'class': 'form-group form-contro rounded-pill',
            'placeholder': 'Data de Publicação',
        }
    ), label='')

    def __init__(self, usuario=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # TODO: entender da onde vem esse 'self.usuario'
        self.receita = receita

    class Meta:
        model = models.Receita
        fields = '__all__'
        exclude = ('slug')