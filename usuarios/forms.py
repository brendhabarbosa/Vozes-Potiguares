from django import forms 
from usuarios.models import Usuario
import json
import os
class UsuarioForm(forms.ModelForm):
    class Meta: 
        model = Usuario 
        fields = ['nome_completo', 'username','data_nascimento', 'cidade','email','senha']
        widgets = {
            'nome_completo': forms.TextInput(attrs={'class': 'estilouser', 'placeholder': 'Nome Completo'}),
            'username': forms.TextInput(attrs={'class': 'estilouser', 'placeholder': 'Nome de Usuário'}),
            'data_nascimento': forms.DateInput(attrs={'class': 'estilouser', 'type': 'date'}),
            'cidade': forms.Select(attrs={'class': 'estilocidade'}),
            'email': forms.EmailInput(attrs={'class': 'estiloemail', 'placeholder': 'vozesdooestepotiguar@exemplo.com'}),
            'senha': forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': '********'}),
        }


