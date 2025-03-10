from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EstudoViewSet, PontuacaoViewSet, login_usuario

router = DefaultRouter()
router.register(r'estudos', EstudoViewSet, basename="estudo")
router.register(r'pontuacoes', PontuacaoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path("login/", login_usuario, name="login_usuario"),
    path('usuarios/<int:pk>/perfil/', EstudoViewSet.as_view({'get': 'perfil'}), name='usuario-perfil'),]
