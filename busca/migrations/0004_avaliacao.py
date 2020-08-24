# Generated by Django 3.1 on 2020-08-24 21:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('busca', '0003_auto_20200824_0357'),
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
    ]
