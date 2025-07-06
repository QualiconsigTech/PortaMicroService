from django.db import models

class Solicitacao(models.Model):
    PRIORIDADES = [
        ("baixa", "Baixa"),
        ("media", "Média"),
        ("alta", "Alta"),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    usuario_id = models.IntegerField()
    setor_id = models.IntegerField()
    prioridade = models.CharField(max_length=10, choices=PRIORIDADES, default="media")
    aprovado = models.BooleanField(default=False)
    encerrado_em = models.DateTimeField(null=True, blank=True)
    analista_id = models.IntegerField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)


class ComentarioSolicitacao(models.Model):
    solicitacao = models.ForeignKey(Solicitacao, on_delete=models.CASCADE)
    usuario_id = models.IntegerField()  # FK para Usuario (via API)
    mensagem = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
