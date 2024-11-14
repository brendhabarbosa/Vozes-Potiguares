from django.shortcuts import render, redirect
from publicacoes.forms import TextoForm
from django.contrib.admin.views.decorators import staff_member_required
from publicacoes.models import Texto, Revisão
from usuarios.models import Usuario
from datetime import date
# Create your views here.
def exibirtexto(request):
    return render(request, 'publicacoes/exibirtexto.html')

def postagem(request):
    if request.method == 'POST':
        form = TextoForm(request.POST, request.FILES)
        print(form.errors)
        if form.is_valid():
            texto = form.save(commit=False)  # Cria instância sem salvar
            texto.autor = request.user  # Atribui o autor (usuário logado)
            texto.data_de_publicacao = date.today()
            texto.save()  # Salva a notícia no banco
            return redirect('autor')  # Redireciona para página de sucesso
    else:
        form = TextoForm() 

    contexto = {'form': form}
    return render(request, 'publicacoes/postagem.html', contexto)

def revisartexto(request, texto_id):
    texto = Texto.objects.get(id=texto_id)

    context = {
        "texto": texto
    }

    return render(request, 'publicacoes/revisartexto.html', context)

def publicar_texto(request, texto_id):
    usuario = Usuario.objects.get(id=request.user.id)
    texto = Texto.objects.get(id=texto_id)

    Revisão.objects.create(texto=texto, revisor=usuario, publicado=True)
    texto.publicacao = True
    texto.save()

    return redirect('exibirtexto')

def devolver_texto(request, texto_id):
    motivo_devolucao = request.POST.get('motivo_devolucao')

    usuario = Usuario.objects.get(id=request.user.id)
    texto = Texto.objects.get(id=texto_id)

    Revisão.objects.create(texto=texto, revisor=usuario, motivo_devolucao=motivo_devolucao)

    return redirect('analisar_texto')

def textosdevolvidos(request):
    return render(request, 'publicacoes/textosdevolvidos.html')

def textosporcidade(request):
    return render(request, 'publicacoes/textosporcidade.html')

def textosporgenero(request):
    return render(request, 'publicacoes/textosporgenero.html')

@staff_member_required
def analisar_texto(request):
    textos = Texto.objects.filter(publicacao=False)

    context = {
        "textos": textos
    }

    return render(request, 'publicacoes/analisar_texto.html', context)