from rest_framework import viewsets
from rest_framework.response import Response
from django.contrib.auth.models import User
from .models import Estudo, Pontuacao
from .serializers import EstudoSerializer, PontuacaoSerializer

class EstudoViewSet(viewsets.ModelViewSet):
    queryset = Estudo.objects.all()
    serializer_class = EstudoSerializer

    def perform_create(self, serializer):
        estudo = serializer.save()
        pontuacao, created = Pontuacao.objects.get_or_create(usuario=estudo.usuario)
        pontuacao.calcular_pontuacao()

class PontuacaoViewSet(viewsets.ModelViewSet):
    queryset = Pontuacao.objects.all()
    serializer_class = PontuacaoSerializer
