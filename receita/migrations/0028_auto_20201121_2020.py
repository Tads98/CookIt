# Generated by Django 3.1.2 on 2020-11-21 23:20

from django.db import migrations
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0027_auto_20201014_2152'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='slug',
            field=django_extensions.db.fields.AutoSlugField(blank=True, default='SOME STRING', editable=False, populate_from='nome_receita'),
        ),
    ]