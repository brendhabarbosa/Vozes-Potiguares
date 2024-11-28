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
from django.urls import path
from publicacoes.views import *

urlpatterns = [
    path('exibirtexto/', exibirtexto, name='exibirtexto'),
    path('postagem/', postagem, name='postagem'),
    path('revisartexto/<int:texto_id>/', revisartexto, name='revisartexto'),
    path('textosdevolvidos', textosdevolvidos, name='textosdevolvidos'),
    path('textosporcidade/', textosporcidade, name='textosporcidade'),
    path('textosporgenero/', textosporgenero, name='textosporgenero'),
    path('analisar_texto/', lista_textos, name='analisar_texto'),
    path('publicar_texto/<int:texto_id>/', publicar_texto, name='publicar_texto'),
    path('devolver_texto/<int:texto_id>/', devolver_texto, name='devolver_texto')


]