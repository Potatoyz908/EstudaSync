import json
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Estudo, Pontuacao, Usuario
from .serializers import EstudoSerializer, PontuacaoSerializer

@csrf_exempt
def login_usuario(request):
    if request.method == "POST":
        data = json.loads(request.body)
        nome = data.get("nome")

        if not nome:
            return JsonResponse({"erro": "Nome é obrigatório"}, status=400)

        usuario, criado = Usuario.objects.get_or_create(nome=nome)

        return JsonResponse({
            "id": usuario.id,
            "nome": usuario.nome,
            "novo_usuario": criado
        })

class EstudoViewSet(viewsets.ModelViewSet):
    queryset = Estudo.objects.all()
    serializer_class = EstudoSerializer

    def perform_create(self, serializer):
        usuario_id = self.request.data.get("usuario_id")
        usuario = get_object_or_404(Usuario, id=usuario_id)
        serializer.save(usuario=usuario)
        pontuacao, created = Pontuacao.objects.get_or_create(usuario=usuario)
        pontuacao.calcular_pontuacao()

class PontuacaoViewSet(viewsets.ModelViewSet):
    queryset = Pontuacao.objects.all()
    serializer_class = PontuacaoSerializer
