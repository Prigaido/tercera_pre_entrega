from django.shortcuts import render
from .models import Curso, Alumnos, Entregable, Profesores
from django.http import HttpResponse
from .forms import ProfeForm, AlumForm, CursoForm, EntregaForm

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

def inicio(request):
    return render(request, "Appproyect/inicio.html")


def profeformulario(request):
    if request.method == "POST":
       form = ProfeForm(request.POST)
       if form.is_valid():
           info = form.cleaned_data
           profe = Profesores(nombre=info["nombre"], apellido=info["apellido"], email=info["email"], profesion=info["profesion"])
           profe.save()
           return render(request, "Appproyect/profesores.html", {"mensaje": "Profe añadido"})
       else:
           return render(request, "Appproyect/profesores.html", {"mensaje": "Datos inválidos"})
    else:
         form = ProfeForm()
         return render(request, "Appproyect/profesores.html", {"formulario": form})
def cursoformulario(request):
    if request.method == "POST":
       form = CursoForm(request.POST)
       if form.is_valid():
           info = form.cleaned_data
           curso = Curso(nombre=info["nombre"], comision=info["comision"])
           curso.save()
           return render(request, "Appproyect/cursos.html", {"mensaje": "Curso añadido"})
       else:
           return render(request, "Appproyect/cursos.html", {"mensaje": "Datos inválidos"})
    else:
         form = CursoForm()
         return render(request, "Appproyect/cursos.html", {"formulario": form})

def alumformulario(request):
    if request.method == "POST":
       form = AlumForm(request.POST)
       if form.is_valid():
           info = form.cleaned_data
           alumnos = Alumnos(nombre=info["nombre"], apellido=info["apellido"], email=info["email"])
           alumnos.save()
           return render(request, "Appproyect/alumnos.html", {"mensaje": "Alumno Registrado"})
       else:
           return render(request, "Appproyect/almunos.html", {"mensaje": "Datos inválidos"})
    else:
         form = AlumForm()
         return render(request, "Appproyect/alumnos.html", {"formulario": form})


def entregaformulario(request):
    if request.method == "POST":
       form = EntregaForm(request.POST)
       if form.is_valid():
           info = form.cleaned_data
           entrega = Entregable(nombre=info["nombre"], fechadeEntrega=info["fechadeEntrega"], entregado=info["entregado"])
           entrega.save()
           return render(request, "Appproyect/entregables.html", {"mensaje": "Entrega realizada"})
       else:
           return render(request, "Appproyect/entregables.html", {"mensaje": "Datos inválidos"})
    else:
         form = EntregaForm()
         return render(request, "Appproyect/entregables.html", {"formulario": form})

def alumnos(request):
    return render(request, "Appproyect/alumnos.html")

def profesores(request):
    return render(request, "Appproyect/profesores.html")

def entregables(request):
    return render(request, "Appproyect/entregables.html")

def cursos(request):
    curso = Curso.objects.all()
    return render(request, "Appproyect/cursos.html", {"cursos":curso})






def busquedaComision(request):
    return render(request, "Appproyect/busquedaComision.html")

def buscar(request):
    comision=request.GET["comision"]
    if comision!="":
        cursos= Curso.objects.filter(comision__incontains=comision)
        return render(request, "Appproyect/busquedaComision.html", {"cursos":cursos})
    else:
        return render(request, "Appproyect/busquedaComision.html", {"mensaje": "No ingresaste datos"})