from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from usuarios.forms import UsuarioForm
from usuarios.models import Usuario
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, 'usuarios/index.html')

@login_required(login_url='/paginadelogin')
def autor(request):
    usuario = Usuario.objects.get(username=request.user.username)

    return render(request, 'usuarios/autor.html', context={ 'user': usuario })

def autor_obras(request):
    return render(request, 'usuarios/autor_obras.html')

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