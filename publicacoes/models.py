from django.db import models
from usuarios.models import Usuario
# Create your models here.
class Classificação_indicativa(models.Model):
    idade = models.IntegerField(blank=False)

class Genero(models.Model):
    nome = models.CharField(max_length=100, blank=False) 
    def __str__(self):
        return self.nome

class Texto(models.Model):
    autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=100,blank=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    classificacao = models.ForeignKey(Classificação_indicativa, on_delete=models.CASCADE)
    conteudo = models.TextField(blank=False)
    data_de_publicacao = models.DateField(blank=False)
    publicacao = models.BooleanField(default=False)
    def __str__(self):
        return self.titulo

class Revisão(models.Model):
    texto = models.ForeignKey(Texto, on_delete=models.CASCADE, blank=False)
    revisor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=False)
    motivo_devolucao = models.TextField()

    def __str__(self):
        return self.texto.titulo
    
class Curtidas(models.Model):
    texto = models.ForeignKey(Texto, on_delete=models.CASCADE)
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
