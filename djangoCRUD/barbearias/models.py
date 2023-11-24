from django.db import models

# Create your models here.

class Barbearia(models.Model):
    nome = models.CharField(max_length=100)
    endereco = models.CharField(max_length=200)
    funcionarios = models.PositiveIntegerField()

    def __str__(self):
        return self.nome
