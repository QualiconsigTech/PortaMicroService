from .models import Mensagem
from .serializers import MensagemSerializer
from rest_framework.exceptions import ValidationError

def enviar_mensagem(data):
    serializer = MensagemSerializer(data=data)
    serializer.is_valid(raise_exception=True)
    return serializer.save()

def listar_conversa(usuario1_id, usuario2_id):
    return Mensagem.objects.filter(
        usuario_origem_id__in=[usuario1_id, usuario2_id],
        usuario_destino_id__in=[usuario1_id, usuario2_id]
    ).order_by('enviada_em')
