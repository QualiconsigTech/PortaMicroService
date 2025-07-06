import requests
from .models import LogIntegracao
from .serializers import LogIntegracaoSerializer

def disparar_integracao(data):
    metodo = data.get('metodo', 'POST').upper()
    url = data['endpoint']
    payload = data.get('payload_enviado', {})

    try:
        resposta = requests.request(method=metodo, url=url, json=payload)
        log = LogIntegracao.objects.create(
            nome_sistema=data.get('nome_sistema', 'externo'),
            endpoint=url,
            metodo=metodo,
            payload_enviado=payload,
            resposta_status=resposta.status_code,
            resposta_corpo=resposta.text
        )
    except Exception as e:
        log = LogIntegracao.objects.create(
            nome_sistema=data.get('nome_sistema', 'externo'),
            endpoint=url,
            metodo=metodo,
            payload_enviado=payload,
            resposta_status=500,
            resposta_corpo=str(e)
        )
    return log


def listar_logs():
    return LogIntegracao.objects.all().order_by('-criado_em')