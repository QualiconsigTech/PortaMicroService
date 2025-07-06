from django.db import models

class Mensagem(models.Model):
    usuario_origem_id = models.IntegerField()
    usuario_destino_id = models.IntegerField()
    conteudo = models.TextField()
    visualizada = models.BooleanField(default=False)
    enviada_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"De {self.usuario_origem_id} para {self.usuario_destino_id}"

