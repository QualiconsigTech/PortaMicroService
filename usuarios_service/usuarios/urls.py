from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()
router.register(r'usuarios', UsuarioViewSet, basename='usuarios')

urlpatterns = [
    path('', include(router.urls)),
    path('login/', LoginView.as_view(), name='login'),
    path('me/', UsuarioLogadoView.as_view(), name='usuario_me'),
    path('senha/', AtualizarSenhaView.as_view(), name='atualizar_senha'),
    path('<int:id>/dados_basicos/', UsuarioDadosBasicosView.as_view(), name='usuario_dados_basicos'),
]