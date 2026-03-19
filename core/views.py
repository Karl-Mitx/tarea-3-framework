from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages

from universidad.Models.Alumno.models import Alumno
from .models import Catedratico, Curso, Nota, InscripcionAlumno, AsignacionCurso
from .forms import CatedraticoForm, CursoForm, NotaForm, InscripcionAlumnoForm, AsignacionCursoForm


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

def notas_view(request):
    notas = Nota.objects.all()
    return render(request, 'core/notas_list.html', {'notas': notas})


def nota_create(request):
    form = NotaForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Nota registrada correctamente.')
        return redirect('core:notas')
    return render(request, 'core/notas.html', {
        'form': form,
        'title': 'Nueva Nota'
    })


def nota_detail(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    return render(request, 'core/notas_detail.html', {'nota': nota})


def nota_edit(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    form = NotaForm(request.POST or None, instance=nota)
    if form.is_valid():
        form.save()
        messages.success(request, 'Nota actualizada correctamente.')
        return redirect('core:notas')
    return render(request, 'core/notas.html', {
        'form': form,
        'title': 'Editar Nota'
    })


def nota_delete(request, pk):
    nota = get_object_or_404(Nota, pk=pk)
    if request.method == 'POST':
        nota.delete()
        messages.success(request, 'Nota eliminada correctamente.')
        return redirect('core:notas')
    return render(request, 'core/notas_confirm_delete.html', {
        'nota': nota
    })

def inscripciones_view(request):
    inscripciones = InscripcionAlumno.objects.all()
    return render(request, 'core/inscripciones_list.html', {'inscripciones': inscripciones})


def inscripcion_create(request):
    form = InscripcionAlumnoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Inscripción registrada correctamente.')
        return redirect('core:inscripciones')
    return render(request, 'core/inscripciones.html', {
        'form': form,
        'title': 'Nueva Inscripción'
    })


def inscripcion_detail(request, pk):
    inscripcion = get_object_or_404(InscripcionAlumno, pk=pk)
    return render(request, 'core/inscripcion_detail.html', {'inscripcion': inscripcion})


def inscripcion_edit(request, pk):
    inscripcion = get_object_or_404(InscripcionAlumno, pk=pk)
    form = InscripcionAlumnoForm(request.POST or None, instance=inscripcion)
    if form.is_valid():
        form.save()
        messages.success(request, 'Inscripción actualizada correctamente.')
        return redirect('core:inscripciones')
    return render(request, 'core/inscripciones.html', {
        'form': form,
        'title': 'Editar Inscripción'
    })


def inscripcion_delete(request, pk):
    inscripcion = get_object_or_404(InscripcionAlumno, pk=pk)
    if request.method == 'POST':
        inscripcion.delete()
        messages.success(request, 'Inscripción eliminada correctamente.')
        return redirect('core:inscripciones')
    return render(request, 'core/inscripcion_confirm_delete.html', {
        'inscripcion': inscripcion
    })

def asignaciones_view(request):
    asignaciones = AsignacionCurso.objects.all()
    return render(request, 'core/asignaciones_list.html', {'asignaciones': asignaciones})


def asignacion_create(request):
    form = AsignacionCursoForm(request.POST or None)
    if form.is_valid():
        form.save()
        messages.success(request, 'Asignación registrada correctamente.')
        return redirect('core:asignaciones')
    return render(request, 'core/asignacion_form.html', {
        'form': form,
        'title': 'Nueva Asignación'
    })


def asignacion_detail(request, pk):
    asignacion = get_object_or_404(AsignacionCurso, pk=pk)
    return render(request, 'core/asignacion_detail.html', {'asignacion': asignacion})


def asignacion_edit(request, pk):
    asignacion = get_object_or_404(AsignacionCurso, pk=pk)
    form = AsignacionCursoForm(request.POST or None, instance=asignacion)
    if form.is_valid():
        form.save()
        messages.success(request, 'Asignación actualizada correctamente.')
        return redirect('core:asignaciones')
    return render(request, 'core/asignacion_form.html', {
        'form': form,
        'title': 'Editar Asignación'
    })


def asignacion_delete(request, pk):
    asignacion = get_object_or_404(AsignacionCurso, pk=pk)
    if request.method == 'POST':
        asignacion.delete()
        messages.success(request, 'Asignación eliminada correctamente.')
        return redirect('core:asignaciones')
    return render(request, 'core/asignacion_confirm_delete.html', {
        'asignacion': asignacion
    })