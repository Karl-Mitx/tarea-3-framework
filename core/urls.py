from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cursos/', views.cursos_view, name='cursos'),

    path('catedraticos/', views.catedraticos_view, name='catedraticos'),
    path('catedraticos/crear/', views.catedratico_create, name='catedratico_create'),
    path('catedraticos/<int:pk>/', views.catedratico_detail, name='catedratico_detail'),
    path('catedraticos/<int:pk>/editar/', views.catedratico_edit, name='catedratico_edit'),
    path('catedraticos/<int:pk>/eliminar/', views.catedratico_delete, name='catedratico_delete'),

    path('notas/', views.notas_view, name='notas'),
]