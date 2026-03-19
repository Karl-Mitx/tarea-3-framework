from django import forms
from .models import Catedratico


class CatedraticoForm(forms.ModelForm):
    class Meta:
        model = Catedratico
        fields = ['primer_nombre', 'segundo_nombre', 'email']
        widgets = {
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }