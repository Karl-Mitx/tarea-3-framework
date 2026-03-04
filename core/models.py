from django.db import models

class Curso(models.Model):
    nombre = models.CharField(max_length=150)
    codigo = models.CharField(max_length=20, unique=True)
    creditos = models.IntegerField()

    def __str__(self):
        return self.nombre

    class Meta:
        db_table = 'curso'