from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from universidad.Models.Alumno.models import Alumno
from .models import Catedratico, Curso
from .forms import CatedraticoForm, CursoForm


def dashboard(request):
    context = {
        'total_alumnos': Alumno.objects.count(),
        'activos': Alumno.objects.filter(is_active=True).count(),
        'inactivos': Alumno.objects.filter(is_active=False).count(),
    }

    return render(request, 'core/dashboard.html', context)


def cursos_view(request):
    cursos = Curso.objects.all()
    return render(request, 'core/cursos_list.html', {'cursos': cursos})


def curso_create(request):
    form = CursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Curso registrado correctamente.')
        return redirect('core:cursos')
    return render(request, 'core/cursos.html', {
        'form': form,
        'title': 'Nuevo Curso'
    })


def curso_detail(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    return render(request, 'core/cursos_detail.html', {'curso': curso})


def curso_edit(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    form = CursoForm(request.POST or None, instance=curso)
    if form.is_valid():
        form.save()
        messages.success(request, 'Curso actualizado correctamente.')
        return redirect('core:cursos')
    return render(request, 'core/cursos.html', {
        'form': form,
        'title': 'Editar Curso'
    })


def curso_delete(request, pk):
    curso = get_object_or_404(Curso, pk=pk)
    if request.method == 'POST':
        curso.delete()
        messages.success(request, 'Curso eliminado correctamente.')
        return redirect('core:cursos')
    return render(request, 'core/cursos_confirm_delete.html', {
        'curso': curso
    })


def catedraticos_view(request):
    catedraticos = Catedratico.objects.all()
    return render(request, 'core/catedraticos.html', {'catedraticos': catedraticos})


def catedratico_create(request):
    form = CatedraticoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Catedrático registrado correctamente.')
        return redirect('core:catedraticos')
    return render(request, 'core/catedratico_form.html', {
        'form': form,
        'title': 'Nuevo Catedrático'
    })


def catedratico_detail(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    return render(request, 'core/catedratico_detail.html', {'catedratico': catedratico})


def catedratico_edit(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    form = CatedraticoForm(request.POST or None, instance=catedratico)
    if form.is_valid():
        form.save()
        messages.success(request, 'Catedrático actualizado correctamente.')
        return redirect('core:catedraticos')
    return render(request, 'core/catedratico_form.html', {
        'form': form,
        'title': 'Editar Catedrático'
    })


def catedratico_delete(request, pk):
    catedratico = get_object_or_404(Catedratico, pk=pk)
    if request.method == 'POST':
        catedratico.delete()
        messages.success(request, 'Catedrático eliminado correctamente.')
        return redirect('core:catedraticos')
    return render(request, 'core/catedratico_confirm_delete.html', {
        'catedratico': catedratico
    })


def inscripciones_view(request):
    return render(request, 'core/inscripciones.html')


def notas_view(request):
    return render(request, 'core/notas.html')