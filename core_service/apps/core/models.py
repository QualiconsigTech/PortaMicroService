from django.db import models

class Grupo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome


class Setor(models.Model):
    nome = models.CharField(max_length=100)
    grupo = models.ForeignKey(Grupo, on_delete=models.CASCADE, related_name='setores')

    def __str__(self):
        return self.nome


class Cargo(models.Model):
    nome = models.CharField(max_length=100)

    def __str__(self):
        return self.nome
