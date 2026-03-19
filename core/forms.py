from django import forms
from .models import Catedratico, Curso, Nota, InscripcionAlumno, AsignacionCurso


class CatedraticoForm(forms.ModelForm):
    class Meta:
        model = Catedratico
        fields = ['primer_nombre', 'segundo_nombre', 'email']
        widgets = {
            'primer_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'segundo_nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class CursoForm(forms.ModelForm):
    class Meta:
        model = Curso
        fields = ['nombre', 'codigo', 'creditos']
        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'codigo': forms.TextInput(attrs={'class': 'form-control'}),
            'creditos': forms.NumberInput(attrs={'class': 'form-control'}),
        }


class AsignacionCursoForm(forms.ModelForm):
    class Meta:
        model = AsignacionCurso
        fields = ['curso', 'catedratico', 'horario']
        widgets = {
            'curso': forms.Select(attrs={'class': 'form-select'}),
            'catedratico': forms.Select(attrs={'class': 'form-select'}),
            'horario': forms.TextInput(attrs={'class': 'form-control'}),
        }


class InscripcionAlumnoForm(forms.ModelForm):
    class Meta:
        model = InscripcionAlumno
        fields = ['alumno', 'asignacion_curso']
        widgets = {
            'alumno': forms.Select(attrs={'class': 'form-select'}),
            'asignacion_curso': forms.Select(attrs={'class': 'form-select'}),
        }


class NotaForm(forms.ModelForm):
    class Meta:
        model = Nota
        fields = ['inscripcion_alumno', 'nota']
        widgets = {
            'inscripcion_alumno': forms.Select(attrs={'class': 'form-select'}),
            'nota': forms.NumberInput(attrs={'class': 'form-control', 'step': '0.01'}),
        }