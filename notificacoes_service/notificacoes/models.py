from django.db import models

class Notificacao(models.Model):
    usuario_origem_id = models.IntegerField()
    usuario_destino_id = models.IntegerField()
    titulo = models.CharField(max_length=255)
    mensagem = models.TextField()
    lida = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.titulo
