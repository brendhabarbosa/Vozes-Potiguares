from django.shortcuts import render, redirect
from usuarios.forms import UsuarioForm
# Create your views here.
def index(request):
    return render(request, 'usuarios/index.html')

def autor(request):
    return render(request, 'usuarios/autor.html')

def autor_obras(request):
    return render(request, 'usuarios/autor_obras.html')

def cadastro(request):
    form = UsuarioForm()
    if request.method == 'POST':
        form = UsuarioForm(request.POST)
        if form.is_valid():
             form.save()
             return redirect('paginadelogin')
    return render(request, 'usuarios/cadastro.html', {'form': form})

def paginadelogin(request):
    return render(request, 'usuarios/paginadelogin.html')