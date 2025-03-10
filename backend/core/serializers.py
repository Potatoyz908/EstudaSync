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
    tempo_total_estudo = serializers.SerializerMethodField()
    progresso_porcentagem = serializers.SerializerMethodField()

    class Meta:
        model = Usuario
        fields = ['id', 'nome', 'tempo_total_estudo', 'progresso_porcentagem'] 

    def get_tempo_total_estudo(self, obj):
        total_minutos = Estudo.objects.filter(usuario=obj).aggregate(total=models.Sum('tempo_estudado'))['total'] or 0
        horas = total_minutos // 60
        minutos = total_minutos % 60
        return f"{horas:02}:{minutos:02}:00"

    def get_progresso_porcentagem(self, obj):
        total_minutos = Estudo.objects.filter(usuario=obj).aggregate(total=models.Sum('tempo_estudado'))['total'] or 0
        total_horas = total_minutos / 60
        return min((total_horas / 1067) * 100, 100)