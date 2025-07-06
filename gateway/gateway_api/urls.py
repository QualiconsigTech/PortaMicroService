from django.urls import path
from gateway_api.views import *
from .views import *

urlpatterns = [
    path('usuarios/<int:id>/', UsuarioPorIdProxyView.as_view(), name='usuario_por_id'),
    path('usuarios/login/', LoginProxyView.as_view(), name='login_proxy'),
    path('chamados/criar/', CriarChamadoProxyView.as_view(), name='criar_chamado'),
]