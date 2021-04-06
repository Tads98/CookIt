from receita.models import Receita, Ingrediente, Avaliacao
from django.contrib.auth.models import User
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
#    receita = ReceitasSerializer(many=True)
    class Meta:
        model = User
        fields = '__all__'
    depth = 1

class IngredienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ingrediente
        fields = '__all__'

class ReceitaSerializer(serializers.ModelSerializer):
#    dono_receita = serializers.SlugRelatedField(
#        many=False,
#        read_only=True,
#        slug_field='first_name'
#    )
    dono_receita = UserSerializer(many=False)
    ingredientes = IngredienteSerializer(many=True)
    class Meta:
        model = Receita
        fields = '__all__'

class PostReceitaSerializer(serializers.ModelSerializer):
    ingredientes = IngredienteSerializer(many=True)
    class Meta:
        model = Receita
        fields = '__all__'

    def create(self, validated_data):
        ingredientes_data = validated_data.pop('ingredientes')
        receita = Receita.objects.create(**validated_data)
        i = []

        for ingrediente in ingredientes_data:
            a = Ingrediente.objects.create(**ingrediente)
            i.append(a.id)
        
        receita.ingredientes.set(tuple(i))
        return receita


class AvaliacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Avaliacao
        fields = '__all__'