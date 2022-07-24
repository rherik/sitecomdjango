from django.db import models
from django.utils import timezone


# Create your models here.


class Categoria(models.Model):
    nome = models.CharField(max_length=55)

    def __str__(self):
        return self.nome


class ListaDosFilmes(models.Model):
    nome = models.CharField(max_length=255)
    direcao = models.CharField(max_length=55, blank=True)
    ano = models.CharField(max_length=25)
    data_criacao = models.DateTimeField(default=timezone.now)
    resumo = models.TextField(blank=True)
    genero = models.CharField(max_length=55)
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING)

    def __str__(self):
        return self.nome
