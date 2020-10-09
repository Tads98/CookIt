from os import error
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from . import models

class ReceitaForm(forms.ModelForm):

    nome_receita = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-group form-control rounded-pill',
            'placeholder': 'Nome da Receita',
        }
    ), label='')

    modo_preparo = forms.IntegerField(widget=forms.Textarea(
        attrs={
            'class': 'form-group form-control',
            'placeholder': 'Modo de Preparo',
        }
    ), label='')

    tempo_preparo = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class': 'form-group form-control rounded-pill',
            'placeholder': 'Tempo de Preparo',
        }
    ), label='')

    porcoes = forms.CharField(widget=forms.NumberInput(
        attrs={
            'class': 'form-group form-control rounded-pill',
            'placeholder': 'Porções',
        }
    ), label='')

    tempo_unidade_medida = forms.ChoiceField(
        choices=(
            ('M', 'Minuto'),
            ('H', 'Hora'),
            ('D', 'Dias'),
        ),
        widget=forms.Select(
            attrs={
                'class': 'form-group form-control rounded-pill',
                'placeholder': 'Unidade de Tempo',
            }
        ), 
        label='')

    dono_receita = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-group form-control rounded-pill',
            'placeholder': 'Chef',
        }
    ), label='')

    fotos = forms.ImageField(widget=forms.FileInput(
        attrs={
            'class': 'form-group',
            'placeholder': 'Fotos',
        }
    ), label='')

    dificuldade = forms.ChoiceField(
        choices=(
            ('F', 'Fácil'),
            ('M', 'Médio'),
            ('D', 'Difícil'),
            ('C', 'Master Chef'),

        ),
        widget=forms.Select(
            attrs={
                'class': 'form-group form-control rounded-pill',
                'placeholder': 'Dificuldade',
            }
        ), 
        label='Dificuldade')

    sabor_receita = forms.ChoiceField(
        choices={
            ('D', 'Doce'), ('S', 'Salgado')
        },
        widget=forms.Select(
            attrs={
                'class': 'form-group form-control rounded-pill',
                'placeholder': 'Dificuldade',
            }
        ),
        label='Sabor')

#    def __init__(self, usuario=None, *args, **kwargs):
#        super().__init__(*args, **kwargs)
#        # TODO: entender da onde vem esse 'self.usuario'
#        self.receita = receita

    class Meta:
        model = models.Receita
        fields = '__all__'
        exclude = ('slug', 'data_publicacao')