# Generated by Django 3.0.7 on 2020-10-07 21:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0017_auto_20200928_1956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='data_publicacao',
            field=models.DateTimeField(verbose_name='data_publicacao'),
        ),
    ]