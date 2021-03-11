from receita.models import Receita

from rest_framework import serializers

class ReceitaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Receita
        fields = '__all__'