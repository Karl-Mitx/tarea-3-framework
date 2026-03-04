from django.db import models

from universidad.Models.Alumno.models import Alumno


class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'curso'

class Catedratico(models.Model):
    primer_nombre = models.CharField(max_length=100)
    segundo_nombre = models.CharField(max_length=100)
    email = models.EmailField(unique=True)

    def __str__(self):
        return f"{self.primer_nombre} {self.segundo_nombre}"

    class Meta:
        db_table = 'catedratico'

class AsignacionCurso(models.Model):
    curso = models.ForeignKey(Curso, on_delete=models.CASCADE)
    catedratico = models.ForeignKey(Catedratico, on_delete=models.CASCADE)
    horario = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.curso.nombre} - {self.catedratico.primer_nombre} {self.catedratico.segundo_nombre}"

    class Meta:
        db_table = 'asignacion_curso'


class InscripcionAlumno(models.Model):
    alumno = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    asignacion_curso = models.ForeignKey(AsignacionCurso, on_delete=models.CASCADE)
    fecha_inscripcion = models.DateField(auto_now_add=True)

    class Meta:
        db_table = 'inscripcion_alumno'