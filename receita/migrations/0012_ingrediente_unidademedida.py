# Generated by Django 3.1 on 2020-09-14 21:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0011_auto_20200911_2223'),
    ]

    operations = [
        migrations.AddField(
            model_name='ingrediente',
            name='unidadeMedida',
            field=models.CharField(choices=[('X', 'Xícara'), ('C', 'Colher de Sopa'), ('D', 'Dente de Alho'), ('M', 'ML'), ('L', 'Litros')], default='X', max_length=1),
        ),
    ]