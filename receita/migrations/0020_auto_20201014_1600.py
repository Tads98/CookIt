# Generated by Django 3.1.2 on 2020-10-14 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('receita', '0019_auto_20201012_2314'),
    ]

    operations = [
        migrations.AlterField(
            model_name='receita',
            name='fotos',
            field=models.ImageField(blank=True, null=True, upload_to='receita/media'),
        ),
    ]