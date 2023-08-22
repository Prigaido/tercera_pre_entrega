from django.shortcuts import render
from .models import Curso
from django.http import HttpResponse

# Create your views here.

def crear_curso(request):

    nombre_curso = "Desarrollo de Apps"
    comision_curso = 4569
    print("Creando Curso...")
    curso = Curso(nombre = nombre_curso, comision = comision_curso)
    curso.save()
    respuesta = f"Curso Creado: {curso.nombre} - {curso.comision}"
    return HttpResponse(respuesta)

def listar_cursos(request):
    cursos = Curso.objects.all()
    respuesta = ""
    for curso in cursos:
        respuesta = f"{curso.nombre} - {curso.comision}<br>"
    return HttpResponse(respuesta)