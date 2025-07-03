from django.db import models

class Chamado(models.Model):
    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    criado_em = models.DateTimeField(auto_now_add=True)
    editado_em = models.DateTimeField(auto_now=True)
    encerrado_em = models.DateTimeField(null=True, blank=True)
    solucao = models.TextField(null=True, blank=True)
    arquivos = models.JSONField(default=list, blank=True)

    analista_id = models.BigIntegerField(null=True, blank=True)
    categoria_id = models.BigIntegerField(null=True, blank=True)
    setor_id = models.BigIntegerField(null=True, blank=True)
    usuario_id = models.BigIntegerField()
    prioridade_id = models.BigIntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.titulo} - {self.usuario_id}"
