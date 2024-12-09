from django.contrib import admin
from usuarios.models import Usuario, Seguidor_seguindo, Cidade
# Register your models here.
admin.site.register(Usuario)
admin.site.register(Seguidor_seguindo)
admin.site.register(Cidade)
