from django import forms
from .models import Comentario

class ComentarioForm(forms.ModelForm):
    class Meta:
        model = Comentario
        fields = ['nombre', 'comentario']
        labels = {
            'nombre': 'Nombre',
            'comentario': 'Comentario',

        }
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'comentario': forms.TextInput(attrs={'class': 'form-control'}),
        }