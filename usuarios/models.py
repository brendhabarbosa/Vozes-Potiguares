from django.db import models
# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=100,blank=False)
    brasao = models.ImageField(upload_to="cidades/")

class Usuario(models.Model):
    nome_completo = models.CharField(max_length=100, blank=False, unique=True)
    username = models.CharField(max_length=50, blank=False, unique=True)
    data_nascimento = models.DateField(blank=False)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE)
    email = models.EmailField(blank=False, unique=True)
    senha = models.CharField(max_length=50, blank=False)
    sobre = models.TextField(blank=False)
    avatar = models.ImageField(upload_to="usuarios/") 
    is_admin = models.BooleanField(default=False)

    def __str__(self):
        return self.nome_completo

class Seguidor_seguindo(models.Model):
    id_seguidor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='id_seguidor')
    id_seguindo = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='id_seguindo')

