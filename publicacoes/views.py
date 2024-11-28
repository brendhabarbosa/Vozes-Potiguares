from django.shortcuts import render, redirect
from publicacoes.forms import TextoForm
from django.contrib.admin.views.decorators import staff_member_required
from publicacoes.models import Texto, Revisão
from usuarios.models import Usuario
from datetime import date
from django.core.paginator import Paginator
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

def lista_textos(request):
    textos_lista = Texto.objects.all().order_by('titulo')
    paginator = Paginator(textos_lista, 2)  
    
    page = request.GET.get('page', 1)
    try:
        textos = paginator.page(page)
    except:
        textos = paginator.page(1)
    
    return render(request, 'publicacoes/analisar_texto.html', {
        'textos': textos
    })

def textosdevolvidos(request):
    return render(request, 'publicacoes/textosdevolvidos.html')

def textosporcidade(request):
    obras_lista = Texto.objects.filter(publicacao=True)
    page = 1

    paginator = Paginator(obras_lista, 6)

    try:
        obras = paginator.get_page(page)
    except:
        obras = paginator.get_page(1)

    return render(request, 'publicacoes/textosporcidade.html', { 'obras': obras })

def textosporgenero(request):
    obras_lista = Texto.objects.filter(publicacao=True)
    page = 1

    paginator = Paginator(obras_lista, 6)

    try:
        obras = paginator.get_page(page)
    except:
        obras = paginator.get_page(1)

    return render(request, 'publicacoes/textosporgenero.html', { 'obras': obras })

@staff_member_required
def analisar_texto(request):
    textos = Texto.objects.filter(publicacao=False)

    context = {
        "textos": textos
    }

    return render(request, 'publicacoes/analisar_texto.html', context)