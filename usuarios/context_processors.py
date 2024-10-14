from usuarios.models import Cidade

def cidades(request):
    return {
        "cidades": Cidade.objects.all()
    }