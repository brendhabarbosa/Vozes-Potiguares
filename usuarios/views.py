from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'usuarios/index.html')

def autor(request):
    return render(request, 'usuarios/autor.html')

def cadastro(request):
    return render(request, 'usuarios/cadastro.html')

def paginadelogin(request):
    return render(request, 'usuarios/paginadelogin.html')