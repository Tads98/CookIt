# Generated by Django 3.1.1 on 2020-09-11 21:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0005_auto_20200911_1849'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='tempo_preparo',
            field=models.TimeField(),
        ),
    ]
