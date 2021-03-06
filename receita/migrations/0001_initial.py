# Generated by Django 3.1.7 on 2021-03-06 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nota', models.FloatField(verbose_name='Nota')),
                ('comentario', models.TextField(blank=True, max_length=200, null=True, verbose_name='Comentário')),
            ],
            options={
                'verbose_name_plural': 'Avaliações',
            },
        ),
        migrations.CreateModel(
            name='Ingrediente',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_ingrediente', models.CharField(max_length=100, verbose_name='Nome Ingrediente:')),
                ('unidade_medida_ingrediente', models.CharField(choices=[('U', 'Unidade'), ('X', 'Xícara'), ('C', 'Colher de Sopa'), ('CH', 'Colher de Chá'), ('D', 'Dente de Alho'), ('M', 'Mililitro(ml)'), ('L', 'Litros'), ('G', 'Gramas(g)'), ('KG', 'Quilograma(kg)'), ('AGS', 'ao gosto')], default='U', max_length=3)),
                ('quantidade_ingrediente', models.PositiveIntegerField(default=0, verbose_name='Quantidade:')),
            ],
            options={
                'verbose_name_plural': 'Ingredientes',
            },
        ),
        migrations.CreateModel(
            name='Receita',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_receita', models.CharField(max_length=255, verbose_name='Nome Receita:')),
                ('modo_preparo', models.TextField(max_length=2000, verbose_name='Modo de Preparo:')),
                ('porcoes', models.PositiveIntegerField(verbose_name='Porções:')),
                ('sabor_receita', models.CharField(choices=[('D', 'Doce'), ('S', 'Salgada')], default='D', max_length=1)),
                ('tempo_preparo', models.PositiveIntegerField(default=0, verbose_name='Tempo de preparo:')),
                ('tempo_unidade_medida', models.CharField(choices=[('M', 'Minuto'), ('H', 'Hora'), ('D', 'Dias')], default='M', max_length=1)),
                ('fotos', models.ImageField(blank=True, null=True, upload_to='receita/media')),
                ('categoria', models.CharField(choices=[('C', 'Café da manhã'), ('A', 'Almoço'), ('L', 'Lanche'), ('J', 'Janta'), ('S', 'Sobremesas'), ('B', 'Bebidas'), ('V', 'Vegana')], default='A', max_length=2)),
                ('dificuldade', models.CharField(choices=[('F', 'Fácil'), ('M', 'Médio'), ('D', 'Difícil'), ('C', 'Master Chef')], default='F', max_length=1)),
                ('data_publicacao', models.DateTimeField(auto_now_add=True)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, default='SOME STRING', editable=False, populate_from='nome_receita')),
                ('observacoes_adicionais', models.TextField(max_length=800, verbose_name='Observações adicionais:')),
                ('dono_receita', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('ingredientes', models.ManyToManyField(to='receita.Ingrediente')),
            ],
            options={
                'verbose_name_plural': 'Receita',
            },
        ),
    ]
