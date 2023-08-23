from django.db import models


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()

    def __str__(self):
        return f"{self.nombre} - {self.comision}"


class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email}"


class Profesores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)
    def __str__(self):
        return f"{self.nombre} - {self.apellido} - {self.email} - {self.profesion}"


class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechadeEntrega = models.DateField(max_length=50)
    entregado = models.BooleanField()
    def __str__(self):
        return f"{self.nombre} - {self.fechadeEntrega} - {self.entregado}"


