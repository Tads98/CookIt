
import random

import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'CookIt.settings')

import django
django.setup()

from receita.models import Receita, Ingrediente
from usuario.models import User
from faker import Faker
fakegen = Faker()

receita = ['SUCO', 'BOLO', 'PASTEL', 'TORTA', 'OMELETE']
modo_preparo = ['Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industrys standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.',
                'It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing',
                'Various versions have evolved over the years, sometimes by accident, sometimes on purpose (injected humour and the like).',
                'There are many variations of passages of Lorem Ipsum available, but the majority have suffered alteration in some form, by injected humour, or randomised words which dont look even slightly believable.',
                'If you are going to use a passage of Lorem Ipsum, you need to be sure there isnt anything embarrassing hidden in the middle of text',
                'It uses a dictionary of over 200 Latin words, combined with a handful of model sentence structures, to generate Lorem Ipsum which looks reasonable. The generated Lorem Ipsum is therefore always free from repetition, injected humour, or non-characteristic words etc.']
porcoes = [1, 2, 3, 4, 5]
sabor = ['D', 'S']
tempo = [1, 2, 3, 4, 5]
tempo_unidade_medida = ['M', 'H', 'D']
dono = [1,2]
dificuldade = ['F', 'M', 'D', 'C']


fake_name = ['Abigail Christian', 'Alan Mora', 'Bryan Castillo', 'Curtis Flores', 'Jeffrey Young']

def add_receita():

    u = User.objects.get(username=random.choice(fake_name))
    r = Receita.objects.get_or_create(nome_receita=random.choice(receita), modo_preparo=random.choice(modo_preparo),
                                      porcoes=random.choice(porcoes), sabor_receita=random.choice(sabor), tempo_preparo=random.choice(tempo), tempo_unidade_medida=random.choice(tempo_unidade_medida),
                                      dono_receita=u, dificuldade=random.choice(dificuldade))[0]  
    r.save()
    return r


def populate(NUM=5):

    for entry in range(NUM):
        receita = add_receita()

        fake_nome = fakegen.name()
        fake_quantidade = [1, 2, 3, 4, 5, 6, 7, 8]
        fake_unidade_medida = ['U','X','C','CH','D','M','L','G','KG','AGS']

        ingredinte = Ingrediente.objects.get_or_create(
            receita=receita, nome_ingrediente=fake_nome, unidadeMedida=random.choice(fake_unidade_medida), quantidade=random.choice(fake_quantidade))
        
        


if __name__ == '__main__':
    print('Inserindo dados falsos... Por favor espere.')
    populate(1000)
    print('Dados falsos inseridos.')
