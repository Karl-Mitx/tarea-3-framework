from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),

    path('cursos/', views.cursos_view, name='cursos'),
    path('cursos/crear/', views.curso_create, name='curso_create'),
    path('cursos/<int:pk>/', views.curso_detail, name='curso_detail'),
    path('cursos/<int:pk>/editar/', views.curso_edit, name='curso_edit'),
    path('cursos/<int:pk>/eliminar/', views.curso_delete, name='curso_delete'),

    path('catedraticos/', views.catedraticos_view, name='catedraticos'),
    path('catedraticos/crear/', views.catedratico_create, name='catedratico_create'),
    path('catedraticos/<int:pk>/', views.catedratico_detail, name='catedratico_detail'),
    path('catedraticos/<int:pk>/editar/', views.catedratico_edit, name='catedratico_edit'),
    path('catedraticos/<int:pk>/eliminar/', views.catedratico_delete, name='catedratico_delete'),

    path('asignaciones/', views.asignaciones_view, name='asignaciones'),
    path('asignaciones/crear/', views.asignacion_create, name='asignacion_create'),
    path('asignaciones/<int:pk>/', views.asignacion_detail, name='asignacion_detail'),
    path('asignaciones/<int:pk>/editar/', views.asignacion_edit, name='asignacion_edit'),
    path('asignaciones/<int:pk>/eliminar/', views.asignacion_delete, name='asignacion_delete'),

    path('inscripciones/', views.inscripciones_view, name='inscripciones'),
    path('inscripciones/crear/', views.inscripcion_create, name='inscripcion_create'),
    path('inscripciones/<int:pk>/', views.inscripcion_detail, name='inscripcion_detail'),
    path('inscripciones/<int:pk>/editar/', views.inscripcion_edit, name='inscripcion_edit'),
    path('inscripciones/<int:pk>/eliminar/', views.inscripcion_delete, name='inscripcion_delete'),

    path('notas/', views.notas_view, name='notas'),
    path('notas/crear/', views.nota_create, name='nota_create'),
    path('notas/<int:pk>/', views.nota_detail, name='nota_detail'),
    path('notas/<int:pk>/editar/', views.nota_edit, name='nota_edit'),
    path('notas/<int:pk>/eliminar/', views.nota_delete, name='nota_delete'),
]