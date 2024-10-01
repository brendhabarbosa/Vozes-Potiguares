from django.db import models

# Create your models here.
class Classificação_indicativa(models.Model):
    idade = models.IntegerField(blank=False)

class Genero(models.Model):
    nome = models.CharField(max_length=100, blank=False) 

class Livro(models.Model):
    autor = models.CharField(max_lenght=100,blank=False)
    titulo = models.CharField(max_lenght=100,blank=False)
    genero = models.ForeignKey(Genero, on_delete=models.CASCADE)
    classificacao = models.ForeignKey(Classificação_indicativa, on_delete=models.CASCADE)
    conteudo = models.TextField(blank=False)
    data_de_publicacao = models.DateField(blank=False)
    publicacao = models.BooleanField(default=False)

class Cidade(models.Model):
    nome = models.CharField(max_lenght=100,blank=False)
    brasao = models.ImageField(upload_to="static/img")

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=100, blank=False)
    username = models.CharField(max_length=50, blank=False)
    data_nascimento = models.DateField(blank=False)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    email = models.EmailField(blank=False)
    senha = models.CharField(max_length=50, blank=False)
    sobre = models.TextField(blank=False)
    avatar = models.ImageField(upload_to="static/img")
    is_admin = models.BooleanField(default=False)

class Revisão(models.Model):
    livro = models.ForeignKey(Livro, on_delete=models.CASCADE, blank=False)
    revisor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    publicado = models.BooleanField(default=False)
    motivo_devolucao = models.TextField()

class Seguidor_seguindo(models.Model):
    id_seguidor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_seguindo = models.ForeignKey(Usuario, on_delete=models.CASCADE)