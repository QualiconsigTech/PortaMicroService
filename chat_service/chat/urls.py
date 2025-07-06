from django.urls import path
from .views import EnviarMensagemView, ConversaEntreUsuariosView

urlpatterns = [
    path('enviar/', EnviarMensagemView.as_view()),
    path('conversa/', ConversaEntreUsuariosView.as_view()),
]
