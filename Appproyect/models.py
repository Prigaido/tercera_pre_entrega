from django.db import models


# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=50)
    comision = models.IntegerField()


class Alumnos(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()


class Profesores(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField()
    profesion = models.CharField(max_length=50)


class Entregable(models.Model):
    nombre = models.CharField(max_length=50)
    fechadeEntrega = models.DateField(max_length=50)
    entregado = models.BooleanField()
