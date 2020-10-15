from os import error
from django import forms
from django.contrib.auth.models import User
from django.forms import fields
from . import models
from django.utils.datastructures import MultiValueDict


class ReceitaForm(forms.ModelForm):

    # TODO: erro ao tentar cadastrar uma receita de mesmo nome, (slug)
    nome_receita = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-group form-control rounded-pill',
            'placeholder': 'Nome da Receita',
        }
    ), label='')

    fotos = forms.ImageField(widget=forms.FileInput, required=False)

    modo_preparo = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-group form-control',
            'placeholder': 'Modo de Preparo',
        }
    ), label='')

    tempo_preparo = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-group form-control rounded-pill',
            'placeholder': 'Tempo de Preparo',
            'id': 'prep-time',
            'type': 'number',
            'min': '1'
        }
    ), label='')

    porcoes = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control rounded-pill',
            'placeholder': 'Porções',
            'id': 'portions',
            'type': 'number',
            'min': '1',
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

    dificuldade = forms.ChoiceField(
        choices=(
            ('F', 'Fácil'),
            ('M', 'Médio'),
            ('D', 'Difícil'),
            ('C', 'Master Chef'),

        ),
        widget=forms.Select(
            attrs={
                'id': 'difficulty',
                'class': 'form-control custom-select rounded-pill'
            }
        ),
        label='Dificuldade')

    sabor_receita = forms.ChoiceField(
        choices={
            ('D', 'Doce'), ('S', 'Salgado')
        },
        widget=forms.RadioSelect(
            attrs={
                'class': 'form-group form-control rounded-pill',
                'placeholder': 'Dificuldade',
                'display': 'inline',
            }
        ),
        label='')

    def __init__(self, receita=None, fotos=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # recebendo como parâmentro requisão do formulário
        self.receita = receita
        self.fotos = fotos

    class Meta:
        model = models.Receita
        fields = '__all__'
        exclude = ('slug', 'dono_receita', 'data_publicacao')

    def clean(self, *args, **kwargs):
        data = self.data
        print(data)
        fotos = self.fotos
        print(fotos)

        # Se todos os campos do formulário for válido ele retorna True e armazena os dados em 'cleaned_data'
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        nome_receita = cleaned.get('nome_receita')
        modo_preparo = cleaned.get('modo_preparo')
        tempo_preparo = cleaned.get('tempo_preparo')
        porcoes = cleaned.get('porcoes')
        tempo_unidade_medida = cleaned.get(
            'tempo_unidade_medida')
        dificuldade = cleaned.get('dificuldade')
        sabor_receita = cleaned.get('sabor_receita')
        sabor_receita = cleaned.get('sabor_receita')
        fotos_receita = cleaned.get('fotos')

        print(f'Nome da receita: {nome_receita}')
        print(f'Modo de preparo: {modo_preparo}')
        print(f'Tempo de preparo: {tempo_preparo}')
        print(f'Porções: {porcoes}')
        print(f'Unidade de medida: {tempo_unidade_medida}')
        print(f'Dificuldade: {dificuldade}')
        print(f'Sabor da receita: {sabor_receita}')
        print(f'Fotos: {fotos_receita}')

        print(f' ')
        print(f'#####################')
        print(f' ')

        # Fazendo checagem de dados

        error_msg_time = 'Tempo inválido, digite um número acima de zero.'

        if self.receita:
            if tempo_preparo < 1:
                validation_error_msgs['tempo_preparo'] = error_msg_time

            if porcoes < 1:
                validation_error_msgs['porcoes'] = error_msg_time

            if validation_error_msgs:
                raise(
                    forms.ValidationError(validation_error_msgs)
                )


class IngredienteForm(forms.ModelForm):

    nome_ingrediente = forms.CharField(widget=forms.TextInput(
        attrs={
            'class': 'form-group form-control rounded-pill',
            'placeholder': 'Ingredientes',
        }
    ), label='')

    unidadeMedida = forms.ChoiceField(
        choices={
            ('U', 'Unidade'),
            ('X', 'Xícara'),
            ('C', 'Colher de Sopa'),
            ('CH', 'Colher de Chá'),
            ('D', 'Dente de Alho'),
            ('M', 'Mililitro(ml)'),
            ('L', 'Litros'),
            ('G', 'Gramas(g)'),
            ('KG', 'Quilograma(kg)'),
            ('AGS', 'ao gosto'),
        },
        widget=forms.Select(
            attrs={
                'id': 'difficulty',
                'class': 'form-control custom-select rounded-pill'
            }
        ),
        label='')
    quantidade = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control rounded-pill',
            'placeholder': 'Porções',
            'id': 'portions',
            'type': 'number',
            'min': '1',
        }
    ), label='')

    class Meta:
        model = models.Ingrediente
        fields = ('nome_ingrediente', 'unidadeMedida', 'quantidade')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # recebendo como parâmentro requisão do formulário

    def clean(self, *args, **kwargs):
        data = self.data
        print(f'Ingrediente form: {data}')
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        nome_ingrediente = cleaned.get('nome_ingrediente')
        unidadeMedida = cleaned.get('unidadeMedida')
        quantidade = cleaned.get('quantidade')

        print(f'Nome do Ingrediente: {nome_ingrediente}')
        print(f'Und de medida: {unidadeMedida}')
        print(f'Quantidade: {quantidade}')
