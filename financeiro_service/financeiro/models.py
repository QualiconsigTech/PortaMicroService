from django.db import models

class Repassse(models.Model):
    usuario_id = models.IntegerField()
    valor = models.DecimalField(max_digits=10, decimal_places=2)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Repasse R${self.valor} para usuario {self.usuario_id}"
