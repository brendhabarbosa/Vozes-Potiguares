from django.shortcuts import render, redirect,  get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from usuarios.forms import UsuarioForm, SobreForm
from usuarios.models import Usuario
from publicacoes.models import Texto
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'usuarios/index.html')

@login_required(login_url='/paginadelogin')
def autor(request):
    usuario = Usuario.objects.get(username=request.user.username)
    edicao = False

    return render(request, 'usuarios/autor.html', context={ 'edicao': edicao})

def editar_perfil(request):
    edicao = True 
    usuario = Usuario.objects.get(id=request.user.id)
    form = SobreForm(initial={'sobre': usuario.sobre})
    if request.method == 'POST':
        form = SobreForm(request.POST, request.FILES, instance=usuario)
        print(form.errors)
        if form.is_valid():
            form.save()
            return redirect('autor')
    return render(request, 'usuarios/autor.html', context={ 'edicao': edicao, 'form': form })

def excluir_sobre(request):
    usuario = Usuario.objects.get(id=request.user.id)
    usuario.sobre = '' 
    usuario.save()
    return redirect('autor')

def autor_obras(request):
    print(request.user.username)
    usuario = Usuario.objects.get(username=request.user.username)
    obras = Texto.objects.filter(autor=usuario)

    print(request.user.pk)
    print(usuario)
    print(obras)

    context = {
        'obras': obras
    }

    return render(request, 'usuarios/autor_obras.html', context=context)

def paginasobre(request):
    return render  (request, 'usuarios/paginasobre.html')

def autor_deslogado(request):
    ...

def cadastro(request):
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
             Usuario.objects.create_user(**form.cleaned_data)
             return redirect('paginadelogin')
    return render(request, 'usuarios/cadastro.html', {'form': form})

def paginadelogin(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        print(username, password)        

        user = authenticate(request, username=username, password=password)
        print(user)
        
        if user:
            login(request, user)
            return redirect('index')  
        else:
            print(messages.error)
            messages.error(request, 'Usuário ou senha inválidos.')
    return render(request, 'usuarios/paginadelogin.html')

@login_required(login_url='/paginadelogin')
def sair(request):
    logout(request)
    return redirect('index')

def excluir_perfil(request,id):
    usuario = Usuario.objects.get(id=id)
    usuario.delete()
    return redirect('autor')