"""
URL configuration for main project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from usuarios.views import *

urlpatterns = [
    path('', index, name='index'),
    path('autor/',autor, name='autor'),
    path('autor/<int:autor_id>/', visitar_autor, name="visitar_autor"),
    path('autor/<int:autor_id>/obras/', visitar_autor_obras, name="visitar_autor_obras"),
    path('editar_perfil/', editar_perfil, name='editar_perfil'),
    path('excluir_sobre/', excluir_sobre, name='excluir_sobre'),
    path('excluir_perfil/<int:id>/',excluir_perfil,name='excluir_perfil'),
    path('cadastro/', cadastro, name='cadastro'),
    path('paginadelogin/', paginadelogin, name='paginadelogin'),
    path('autor/obras', autor_obras, name='autor_obras'),
    path('sair', sair, name='sair'),
    path('paginasobre/',paginasobre, name='paginasobre'),
    path('termosdeuso/',termosdeuso, name='termosdeuso'),
    path('politicadeprivacidade/',politicadeprivacidade, name='politicadeprivacidade'),
    path('', include('publicacoes.urls'))
    
]
