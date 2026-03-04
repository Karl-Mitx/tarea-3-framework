from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('cursos/', views.cursos_view, name='cursos'),
    path('catedraticos/', views.catedraticos_view, name='catedraticos'),
    path('notas/', views.notas_view, name='notas'),
]