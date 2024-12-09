from django.shortcuts import render, redirect
from publicacoes.forms import TextoForm
from django.contrib.admin.views.decorators import staff_member_required
from publicacoes.models import Texto, Revisão, Genero
from usuarios.models import Usuario
from datetime import date
from django.core.paginator import Paginator
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.
def exibirtexto(request, texto_id):
    texto = Texto.objects.get(id=texto_id)

    context = { 'texto': texto }

    return render(request, 'publicacoes/exibirtexto.html', context)


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

    return redirect('exibirtexto', texto_id=texto_id)

def devolver_texto(request, texto_id):
    motivo_devolucao = request.POST.get('motivo_devolucao')

    usuario = Usuario.objects.get(id=request.user.id)
    texto = Texto.objects.get(id=texto_id)

    Revisão.objects.create(texto=texto, revisor=usuario, motivo_devolucao=motivo_devolucao)

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

def textosdevolvidos(request):
    return render(request, 'publicacoes/textosdevolvidos.html')

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
    genero = request.GET.get('genero', None)
    if not genero:
        return HttpResponseBadRequest("O parâmetro 'genero' é obrigatório.")
    
    generos_principais = ["Poemas", "Contos", "Crônicas"]
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

    contexto = {
        'obras': obras,
        'nome_genero': nome_genero,
    }

    return render(request, 'publicacoes/textosporgenero.html', contexto)



@staff_member_required
def analisar_texto(request):
    textos = Texto.objects.filter(publicacao=False)

    context = {
        "textos": textos
    }

    return render(request, 'publicacoes/analisar_texto.html', context)


def listadeautores(request):
    lista_autores = Usuario.objects.all().order_by('nome_completo')
    paginator = Paginator(lista_autores, 9)  
    
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