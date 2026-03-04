from django.shortcuts import render
from universidad.Models.Alumno.models import Alumno
def dashboard(request):
    context = {
        'total_alumnos'   : Alumno.objects.count(),
        'activos'         : Alumno.objects.filter(is_active=True).count(),
        'inactivos'       : Alumno.objects.filter(is_active=False).count(),
    }

    return render(request, 'core/dashboard.html', context)

def cursos_view(request):
    return render(request, 'core/cursos.html')

def catedraticos_view(request):
    return render(request, 'core/catedraticos.html')

def inscripciones_view(request):
    return render(request, 'core/inscripciones.html')

def notas_view(request):
    return render(request, 'core/notas.html')