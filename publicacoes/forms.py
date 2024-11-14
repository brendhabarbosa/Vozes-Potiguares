from django import forms
from publicacoes.models import Texto


class TextoForm(forms.ModelForm):
    
    class Meta:
        model = Texto 
        fields = ['titulo', 'genero', 'classificacao', 'conteudo']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'alinhar', 'placeholder': 'História sem título'}),
            'genero': forms.Select(attrs={'class': 'alinhar'}),
            'classificacao': forms.Select(attrs={'class': 'alinhar'}),
            'conteudo': forms.Textarea(attrs={'class': 'alinhar', 'placeholder': 'Escreva o seu texto aqui'}),

        }