from django.contrib import admin
from django.urls import path, include
from rest_framework_simplejwt.views import TokenRefreshView
from usuarios.views import *

urlpatterns = [
    path('admin/', admin.site.urls),

    # Autenticação via JWT
    path('api/token/', CustomTokenView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/usuarios/', include('usuarios.urls')),
    path('<int:id>/', UsuarioDadosBasicosView.as_view(), name='usuario_detalhes'),


    # Rotas do app de usuários
    path('api/usuarios/', include('usuarios.urls')),
]
