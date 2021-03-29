from receita.models import Receita, Ingrediente, Avaliacao
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
#    receita = ReceitasSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'
    depth = 1

class ReceitaSerializer(serializers.ModelSerializer):
#    dono_receita = serializers.SlugRelatedField(
#        many=False,
#        read_only=True,
#        slug_field='first_name'
#    )
    dono_receita = UserSerializer(many=False)
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