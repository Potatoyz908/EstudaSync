from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudoViewSet, PontuacaoViewSet

router = DefaultRouter()
router.register(r'estudos', EstudoViewSet)
router.register(r'pontuacoes', PontuacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
