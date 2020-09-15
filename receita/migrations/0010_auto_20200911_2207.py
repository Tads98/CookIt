# Generated by Django 3.1.1 on 2020-09-12 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0009_auto_20200911_1902'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Usuario',
        ),
        migrations.AddField(
            model_name='ingrediente',
            name='tempo_unidade_medida',
            field=models.CharField(choices=[('M', 'Minuto'), ('H', 'Hora'), ('D', 'Dias')], default='M', max_length=1),
        ),
    ]