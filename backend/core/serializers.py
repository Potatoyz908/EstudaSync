from rest_framework import serializers
from .models import Estudo, Pontuacao, Usuario

class EstudoSerializer(serializers.ModelSerializer):
    usuario_id = serializers.PrimaryKeyRelatedField(queryset=Usuario.objects.all(), source='usuario')
    class Meta:
        model = Estudo
        fields = ['id', 'usuario_id', 'titulo', 'tempo_estudado', 'data']

class PontuacaoSerializer(serializers.ModelSerializer):
    usuario_nome = serializers.CharField(source='usuario.nome', read_only=True)
    class Meta:
        model = Pontuacao
        fields = '__all__'
class UsuarioSerializer(serializers.ModelSerializer):
    class Meta:
        model = Usuario
        fields = '__all__'
