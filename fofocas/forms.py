from django import forms
from .models import Fofoca

class FofocaForm(forms.ModelForm):
    class Meta:
        model = Fofoca
        fields = ['titulo', 'descricao', 'bairro', 'categoria']
        widgets = {
            'titulo': forms.TextInput(attrs={'class': 'form-control'}),
            'descricao': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            'categoria': forms.Select(attrs={'class': 'form-select'}),
            'bairro': forms.Select(attrs={'class': 'form-select'}),
        }