from django.db import models

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