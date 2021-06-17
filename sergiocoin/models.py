from django.db import models


# Create your models here.
class Pessoa(models.Model):
    nome = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    escolaridade = models.CharField(max_length=150)
    idade = models.IntegerField()