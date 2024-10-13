from django.contrib import admin
from publicacoes.models import Classificação_indicativa, Genero, Texto, Revisão
# Register your models here.
admin.site.register(Classificação_indicativa)
admin.site.register(Genero)
admin.site.register(Texto)
admin.site.register(Revisão)