from django.shortcuts import render, redirect
from publicacoes.forms import TextoForm
from django.contrib.admin.views.decorators import staff_member_required
from publicacoes.models import Texto, Revisão, Genero, Curtidas
from usuarios.models import Usuario, Cidade
from datetime import date
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.db import models

# Create your views here.
def exibirtexto(request, texto_id):
    texto = Texto.objects.get(id=texto_id)
    curtida = Curtidas.objects.filter(texto=texto, usuario=request.user).first()

    context = {
        'texto': texto,
        'curtida': curtida
    }

    return render(request, 'publicacoes/exibirtexto.html', context)

def curtir_texto(request, texto_id):
    texto = Texto.objects.get(id=texto_id)
    usuario = Usuario.objects.get(id=request.user.id)

    curtida = Curtidas.objects.filter(texto=texto, usuario=usuario).first()

    if (curtida):
        curtida.delete()
    else:
        Curtidas.objects.create(texto=texto, usuario=usuario)

    return redirect('exibirtexto', texto_id=texto_id)


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

def editar_texto(request, texto_id):
    obra = Texto.objects.get(id=texto_id)

    if request.method == 'POST':
        form = TextoForm(request.POST, request.FILES, instance=obra)
        if form.is_valid():
            texto = form.save(commit=False)  # Cria instância sem salvar
            texto.data_de_publicacao = date.today()
            texto.devolvido = False
            texto.save()
            # Salva no banco
            return redirect('autor')  # Redireciona para página de sucesso
    else:
        form = TextoForm(instance=obra) 

    contexto = {'form': form}
    return render(request, 'publicacoes/postagem.html', contexto)

def excluir_texto(request, texto_id):
    next = request.GET.get('next', 'index')

    texto = Texto.objects.get(id=texto_id)
    texto.delete()

    return redirect(next)

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
    texto.devolvido = False
    texto.save()

    return redirect('exibirtexto', texto_id=texto_id)

def devolver_texto(request, texto_id):
    motivo_devolucao = request.POST.get('motivo_devolucao')

    usuario = Usuario.objects.get(id=request.user.id)
    texto = Texto.objects.get(id=texto_id)

    Revisão.objects.create(texto=texto, revisor=usuario, motivo_devolucao=motivo_devolucao)
    texto.devolvido = True
    texto.save()

    return redirect('analisar_texto')

def lista_textos(request):
    textos_lista = Texto.objects.all().filter(publicacao=False).order_by('titulo')
    paginator = Paginator(textos_lista, 2)  
    
    page = request.GET.get('page', 1)
    try:
        textos = paginator.page(page)
    except:
        textos = paginator.page(1)
    
    return render(request, 'publicacoes/analisar_texto.html', {
        'textos': textos
    })

def textosdevolvidos(request, texto_id):
    texto = Texto.objects.get(id=texto_id)
    revisao = Revisão.objects.filter(texto=texto, publicado=False).first()

    context = {
        "texto": texto,
        "revisao": revisao
    }

    print(revisao.motivo_devolucao)

    return render(request, 'publicacoes/textosdevolvidos.html', context)

def textosfiltro(request):
    filtro_pesquisa = request.GET.get('search')
    textos = []
    if filtro_pesquisa is not None:
        autores = Usuario.objects.filter(username__icontains=filtro_pesquisa)
        textos = Texto.objects.filter(Q(titulo__icontains=filtro_pesquisa) | Q(autor__in=autores))
    
        print(textos)

    contexto = {
        'textos': textos
    }

    return render(request, 'publicacoes/textosfiltro.html', contexto)

def textosporcidade(request, id):
    cidade = Cidade.objects.get(id=id)
    obras_lista = Texto.objects.filter(publicacao=True, autor__cidade=id)
    page = request.GET.get('page', 1)

    print(obras_lista, id)

    paginator = Paginator(obras_lista, 3)

    try:
        obras = paginator.get_page(page)
    except:
        obras = paginator.get_page(1)   
    
    curtidas_por_obras = Texto.objects.filter(publicacao=True, autor__cidade=id).annotate(total_curtidas=models.Count('curtidas')).order_by('-total_curtidas').filter(total_curtidas__gt=0)

    curtidas = curtidas_por_obras[:3]
    print(curtidas)

    return render(request, 'publicacoes/textosporcidade.html', { 'obras': obras, 'cidade': cidade, 'curtidas': curtidas })

def textosporgenero(request, genero):
    # genero = request.GET.get('genero', None)
    if not genero:
        return HttpResponseBadRequest("O parâmetro 'genero' é obrigatório.")
    
    generos_principais = ["Poemas", "Contos", "Cronicas"]
    genero_obj = Genero.objects.filter(nome=genero).first()
    
    nome_genero = ""
    if genero in generos_principais:
        obras_lista = Texto.objects.filter(publicacao=True, genero=genero_obj.id)
        nome_genero = genero_obj.nome
    else:
        generos_exclusao = Genero.objects.filter(nome__in=generos_principais).values_list('id', flat=True)
        obras_lista = Texto.objects.filter(publicacao=True).exclude(genero__id__in=generos_exclusao)
        nome_genero = "Outros"
        
    
    page = request.GET.get('page', 1)
    paginator = Paginator(obras_lista, 3)

    try:
        obras = paginator.get_page(page)
    except:
        obras = paginator.get_page(1)
    
    curtidas_por_obras = Texto.objects.filter(publicacao=True, genero=genero_obj).annotate(total_curtidas=models.Count('curtidas')).order_by('-total_curtidas').filter(total_curtidas__gt=0)

    curtidas = curtidas_por_obras[:3]
    # contador = 0
    # for curtida_por_obra in curtidas_por_obras:
    #     if contador < 3:
    #         curtidas.append(curtida_por_obra)
    #         contador += 1

    contexto = {
        'obras': obras,
        'nome_genero': nome_genero,
        'curtidas': curtidas
    }

    return render(request, 'publicacoes/textosporgenero.html', contexto)



@staff_member_required
def analisar_texto(request):
    textos = Texto.objects.filter(Q(publicacao=False) & Q(devolvido=False))

    context = {
        "textos": textos
    }

    return render(request, 'publicacoes/analisar_texto.html', context)


def listadeautores(request):
    lista_autores = Usuario.objects.filter(is_superuser=False).order_by('nome_completo')
    paginator = Paginator(lista_autores, 6)  
    
    page = request.GET.get('page', 1)
    try:
        autores = paginator.page(page)
    except:
        autores = paginator.page(1)

    context = {
        "autores": autores
    }

    return render(request, 'publicacoes/listadeautores.html', context)


def visitar_autor(request, autor_id):
    autor = Usuario.objects.get(id=autor_id)

    context = {
        "autor": autor
    }

    return render(request, 'publicacoes/visitar_autor.html', context)