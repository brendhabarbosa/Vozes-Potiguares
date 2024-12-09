from django import forms
from publicacoes.models import Texto


class TextoForm(forms.ModelForm):
    
    class Meta:
        model = Texto 
        fields = ['titulo', 'genero', 'classificacao', 'conteudo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'postagem-form', 'placeholder': 'História sem título'}),
            'genero': forms.Select(attrs={'class': 'alinhar postagem-form'}),
            'classificacao': forms.Select(attrs={'class': 'alinhar postagem-form'}),
            'conteudo': forms.Textarea(attrs={'class': 'alinhar postagem-form', 'placeholder': 'Escreva o seu texto aqui'}),

        }