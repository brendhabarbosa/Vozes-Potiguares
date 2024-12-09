from typing import Any
from django.db import models
from django.contrib.auth.models import AbstractUser, UserManager
# Create your models here.

class Cidade(models.Model):
    nome = models.CharField(max_length=100,blank=False)
    brasao = models.CharField(max_length=100,blank=False)

    def __str__(self):
        return self.nome

class CustomManager(UserManager):
    def create_user(self, username, email, password, **extra_fields):
        user = Usuario(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        print("A")

        return user
    
    def create_super_user(self, username, email, password, **extra_fields):
        user = Usuario(username=username, email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)

        return user

class Usuario(AbstractUser):
    nome_completo = models.CharField(max_length=100, blank=False)
    data_nascimento = models.DateField(blank=False, null=True)
    cidade = models.ForeignKey(Cidade, on_delete=models.CASCADE, null=True)
    sobre = models.TextField(blank=False)
    avatar = models.ImageField(upload_to="usuarios/", default='usuarios/default_avatar.png') 

    objects = CustomManager()

    def __str__(self):
        return self.nome_completo

class Seguidor_seguindo(models.Model):
    id_seguidor = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='id_seguidor')
    id_seguindo = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name='id_seguindo')
