import json
from rest_framework import viewsets
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Estudo, Pontuacao, Usuario
from rest_framework.decorators import action
from .serializers import EstudoSerializer, PontuacaoSerializer
from django.db.models import Sum

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
    serializer_class = EstudoSerializer

    def get_queryset(self):
        """
        Retorna os estudos filtrados pelo usuário logado.
        Se nenhum usuário for especificado, retorna todos os estudos.
        """
        queryset = Estudo.objects.all()
        usuario_id = self.request.query_params.get("usuario_id")

        if usuario_id:
            queryset = queryset.filter(usuario__id=usuario_id)

        return queryset

    def perform_create(self, serializer):
        usuario_id = self.request.data.get("usuario_id")
        usuario = get_object_or_404(Usuario, id=usuario_id)
        serializer.save(usuario=usuario)
        pontuacao, created = Pontuacao.objects.get_or_create(usuario=usuario)
        pontuacao.calcular_pontuacao()

    @action(detail=False, methods=["get"])
    def por_usuario(self, request):
        """
        Endpoint para listar os estudos de um usuário específico.
        """
        usuario_id = request.query_params.get("usuario_id")
        if not usuario_id:
            return Response({"erro": "O parâmetro usuario_id é obrigatório"}, status=400)

        estudos = Estudo.objects.filter(usuario__id=usuario_id)
        serializer = EstudoSerializer(estudos, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["get"])
    def perfil(self, request, pk=None):
        """
        Endpoint para exibir o perfil do usuário com tempo total estudado e progresso.
        """
        usuario = get_object_or_404(Usuario, pk=pk)

        # Calculando tempo total estudado
        total_minutos = Estudo.objects.filter(usuario=usuario).aggregate(total=Sum('tempo_estudado'))['total'] or 0        
        horas = total_minutos // 60
        minutos = total_minutos % 60
        tempo_total_formatado = f"{horas:02}:{minutos:02}:00"

        # Calculando progresso
        total_horas = total_minutos / 60
        progresso_porcentagem = min((total_horas / 1067) * 100, 100)  # Garante que não passe de 100%

        return Response({
            "id": usuario.id,
            "nome": usuario.nome,
            "tempo_total_estudo": tempo_total_formatado,
            "progresso_porcentagem": round(progresso_porcentagem, 2)
        })

class PontuacaoViewSet(viewsets.ModelViewSet):
    queryset = Pontuacao.objects.all().select_related("usuario")
    serializer_class = PontuacaoSerializer
