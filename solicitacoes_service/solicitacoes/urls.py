from django.urls import path
from .views import *

urlpatterns = [
    path('criar/', CriarSolicitacaoView.as_view()),
    path('comentarios/', ComentarioSolicitacaoView.as_view()),
    path('<int:solicitacao_id>/aprovar/', AprovarSolicitacaoView.as_view()),
    path('<int:solicitacao_id>/encerrar/', EncerrarSolicitacaoView.as_view()),
]
