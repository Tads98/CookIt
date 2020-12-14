from django.contrib import admin
from . import models


class IngredienteInline(admin.TabularInline):
    model = models.Ingrediente
    extra = 1
    filter_horizontal = ('nome_ingrediente',)

admin.site.register(models.Receita)
admin.site.register(models.Ingrediente)

