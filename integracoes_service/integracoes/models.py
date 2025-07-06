from django.db import models

class LogIntegracao(models.Model):
    nome_sistema = models.CharField(max_length=100)
    endpoint = models.URLField()
    metodo = models.CharField(max_length=10)
    payload_enviado = models.JSONField()
    resposta_status = models.IntegerField(null=True, blank=True)
    resposta_corpo = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.nome_sistema} - {self.endpoint}"
