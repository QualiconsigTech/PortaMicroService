from django.urls import path, include
from rest_framework.routers import DefaultRouter
from chamados.views import *

router = DefaultRouter()
router.register('', ChamadoViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('meus/', MeusChamadosView.as_view(), name='meus_chamados'),
    path('criar/', CriarChamadoView.as_view()),
]
