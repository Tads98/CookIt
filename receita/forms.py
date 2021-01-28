from django import forms
from .models import Receita, Ingrediente
from os import error
from django.forms import fields


class ReceitaForm(forms.ModelForm):

    nome_receita = forms.CharField(widget=forms.TextInput(
    ), label='')

    modo_preparo = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-group form-control',
            'placeholder': '1- Esquente a água...',
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

    sabor_receita = forms.ChoiceField(
        choices={
            ('D', 'Doce'), ('S', 'Salgado')
        },
        widget=forms.RadioSelect(
            attrs={
                'class': 'form-group form-control rounded-pill',
                'display': 'inline',
            }
        ),
        label='')

    tempo_preparo = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-group form-control rounded-pill',
            'placeholder': 'Tempo de Preparo',
            'type': 'number',
            'min': '1'
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

    fotos = forms.ImageField(widget=forms.FileInput, required=False, label='')

    categoria = forms.ChoiceField(
        choices=(
            ('C', 'Café da manhã'),
            ('A', 'Almoço'),
            ('L', 'Lanche'),
            ('J', 'Janta'),
            ('S', 'Sobremesas'),
            ('B', 'Bebidas'),
            ('V', 'Vegana'),

        ),
        widget=forms.Select(
            attrs={
                'class': 'form-control custom-select rounded-pill'
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
                'class': 'form-control custom-select rounded-pill'
            }
        ),
        label='')

    observacoes_adicionais = forms.CharField(widget=forms.Textarea(
        attrs={
            'class': 'form-group form-control',
            'placeholder': '1- Não esquece da deixar massa descançar...',
        }
    ), label='')

    def __init__(self, receita=None, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.receita = receita

    class Meta:
        model = Receita
        fields = '__all__'
        exclude = ('slug', 'dono_receita', 'data_publicacao')

    def clean(self, *args, **kwargs):
        data = self.data

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

    unidade_medida_ingrediente = forms.ChoiceField(
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
                'class': 'form-control custom-select rounded-pill'
            }
        ),
        label='')

    quantidade_ingrediente = forms.IntegerField(widget=forms.NumberInput(
        attrs={
            'class': 'form-control rounded-pill',
            'placeholder': 'Quantidade',
            'type': 'number',
            'min': '1',
        }
    ), label='')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    class Meta:
        model = Ingrediente
        fields = '__all__'

    def clean(self, *args, **kwargs):
        cleaned = self.cleaned_data
        validation_error_msgs = {}

        nome_ingrediente = cleaned.get('nome_ingrediente')
        unidade_medida_ingrediente = cleaned.get('unidade_medida_ingrediente')
        quantidade_ingrediente = cleaned.get('quantidade_ingrediente')

        print(f'Nome do Ingrediente: {nome_ingrediente}')
        print(f'Und de medida: {unidade_medida_ingrediente}')
        print(f'Quantidade: {quantidade_ingrediente}')
