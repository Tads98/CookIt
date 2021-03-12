from receita.models import Receita, Ingrediente, Avaliacao

from rest_framework import serializers

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'