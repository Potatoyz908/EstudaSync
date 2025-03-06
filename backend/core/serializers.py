from rest_framework import serializers
from .models import Estudo, Pontuacao

class EstudoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Estudo
        fields = '__all__'

class PontuacaoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pontuacao
        fields = '__all__'
