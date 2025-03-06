from django.db import models

from django.contrib.auth.models import User
from django.db import models

class Estudo(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=255)  # Nome do vídeo/material estudado
    tempo_estudado = models.PositiveIntegerField(default=0)  # Tempo em minutos
    data = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.usuario.username} - {self.titulo}"

class Pontuacao(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    pontos = models.PositiveIntegerField(default=0)

    def calcular_pontuacao(self):
        estudos = Estudo.objects.filter(usuario=self.usuario)
        total_tempo = sum(estudo.tempo_estudado for estudo in estudos)
        total_materiais = estudos.count()

        self.pontos = (total_tempo // 60) * 10 + total_materiais * 5
        self.save()

    def __str__(self):
        return f"{self.usuario.username} - {self.pontos} pontos"
