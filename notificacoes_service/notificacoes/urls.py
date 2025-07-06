from django.urls import path
from .views import CriarNotificacaoView, MinhasNotificacoesView

urlpatterns = [
    path('criar/', CriarNotificacaoView.as_view()),
    path('listar/', MinhasNotificacoesView.as_view()),
]