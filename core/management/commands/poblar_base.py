from datetime import date, timedelta
import random

from django.core.management.base import BaseCommand
from django.db import transaction

from universidad.Models.Alumno.models import Alumno
from core.models import Catedratico, Curso, AsignacionCurso, InscripcionAlumno, Nota


class Command(BaseCommand):
    help = "Pobla la base de datos con 10K registros de ejemplo"

    @transaction.atomic
    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING("Iniciando carga masiva de datos..."))

        Nota.objects.all().delete()
        InscripcionAlumno.objects.all().delete()
        AsignacionCurso.objects.all().delete()
        Catedratico.objects.all().delete()
        Curso.objects.all().delete()
        Alumno.objects.all().delete()

        cursos = []
        for i in range(1, 21):
            cursos.append(
                Curso.objects.create(
                    nombre=f"Curso {i}",
                    codigo=f"C{i:03d}",
                    creditos=random.randint(2, 6),
                )
            )

        catedraticos = []
        for i in range(1, 51):
            catedraticos.append(
                Catedratico.objects.create(
                    primer_nombre=f"Nombre{i}",
                    segundo_nombre=f"Apellido{i}",
                    email=f"catedratico{i}@universidad.com",
                )
            )

        asignaciones = []
        for i in range(1, 101):
            asignaciones.append(
                AsignacionCurso.objects.create(
                    curso=random.choice(cursos),
                    catedratico=random.choice(catedraticos),
                    horario=random.choice(["07:00-09:00", "09:00-11:00", "13:00-15:00", "18:00-20:00"]),
                )
            )

        alumnos = []
        for i in range(1, 10001):
            alumnos.append(
                Alumno.objects.create(
                    first_name=f"Alumno{i}",
                    last_name=f"Prueba{i}",
                    email=f"alumno{i}@mail.com",
                    is_active=random.choice([True, False]),
                )
            )

        inscripciones = []
        for alumno in alumnos:
            inscripciones.append(
                InscripcionAlumno.objects.create(
                    alumno=alumno,
                    asignacion_curso=random.choice(asignaciones),
                )
            )

        for inscripcion in random.sample(inscripciones, 5000):
            Nota.objects.create(
                inscripcion_alumno=inscripcion,
                nota=round(random.uniform(60, 100), 2),
            )

        self.stdout.write(self.style.SUCCESS("Carga masiva finalizada correctamente."))