from django.shortcuts import render

# Create your views here.
def exibirtexto(request):
    return render(request, 'publicacoes/exibirtexto.html')

def postagem(request):
    return render(request, 'publicacoes/postagem.html')

def revisartexto(request):
    return render(request, 'publicacoes/revisartexto.html')

def textosdevolvidos(request):
    return render(request, 'publicacoes/textosdevolvidos.html')

def textosporcidade(request):
    return render(request, 'publicacoes/textosporcidade.html')

def textosporgenero(request):
    return render(request, 'publicacoes/textosporgenero.html')
