from django.contrib import admin
from . import models


class IngredienteInline(admin.TabularInline):
    model = models.Ingrediente
    extra = 1


class ReceitaAdmin(admin.ModelAdmin):
    inlines = [
        IngredienteInline
    ]


admin.site.register(models.Receita, ReceitaAdmin)
admin.site.register(models.Ingrediente)
