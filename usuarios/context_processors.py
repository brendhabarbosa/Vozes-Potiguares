from usuarios.models import Cidade, Usuario

def cidades(request):
    return {
        "cidades": Cidade.objects.all()
    }

def usuario_processor(request):
    usuario_logado=request.user
    try:
        usuario = Usuario.objects.get(username=request.user.username)
        avatar = f"/media/{usuario.avatar}"
    except Exception:
        avatar = '/static/IMG/icons8-conta-de-teste-60.png'

    return {
        'usuario':usuario_logado,
        'avatar': avatar
    }