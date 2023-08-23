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


def cursoformulario(request):
    if request.method=="POST":
       form = CursoForm(request, "POST")
       if form.is_valid():
           info=form.cleaned_data
           comision = Curso(nombre=info["nombre"], apelllido=info["comision"]),
           comision.save()
           form = CursoForm
           return render(request, "Appproyect/cursoformulario.html", {"mensaje": "Curso Añadido", "form": "CursoForm"})
       else:
           return render(request, "Appproyect/cursoformulario.html", {"mensaje": "Datos Invalidos"})
    else:
        form = CursoForm
        return render(request, "Appproyect/cursoformulario.html", {"formulario": form})
def profeformulario(request):
    if request.method == "POST":
       form = ProfeForm(request.POST)
       if form.is_valid():
           info = form.cleaned_data
           nombre = info["nombre"]
           apellido = info["apellido"]
           email = info["email"]
           profesion = info["profesion"]
           profe = Profesores(nombre=nombre, apelllido=apellido, email=email, profesion=profesion)
           profe.save()
           form=ProfeForm()
           return render(request, "Appproyect/profesores.html", {"mensaje": "Profesor Añadido"})
       else:
            return render(request, "Appproyect/profesores.html", {"mensaje": "Datos Invalidos"})

    else:
        form = ProfeForm()
    return render(request, "Appproyect/profesores.html", {"formulario": form})

def alumformulario(request):
    if request.method=="POST":
       form = AlumForm(request, "POST")

       if form.is_valid():
           info = form.cleaned_data
           alumno = Alumnos(nombre=info["nombre"], apelllido=info["apellido"], email=info["email"])
           alumno.save()
           form = AlumForm
           return render(request, "Appproyect/alumnos.html", {"mensaje": "Alumno Añadido", "form": "AlumForm"})
       else:
           return render(request, "Appproyect/alumnos.html", {"mensaje": "Datos Invalidos"})
    else:
        form = AlumForm
        return render(request, "Appproyect/alumnos.html", {"formulario": form})


def entregaformulario(request):
    if request.method=="POST":
       form=EntregaForm(request, "POST")
       if form.is_valid():
           info=form.cleaned_data
           entrega = Entregable(nombre=info["nombre"], fechadeEntrega=info["fechadeEntrega"], entregado=info["entregado"]),
           entrega.save()
           return render(request, "Appproyect/entregables.html", {"mensaje": "Entraga realizada"})
       else:
           return render(request, "Appproyect/entregables.html", {"mensaje": "Datos Invalidos"})
    else:
         form = EntregaForm
         return render(request, "Appproyect/entregables.html", {"formulario": form})

def alumnos(request):
    return render(request, "Appproyect/alumnos.html")

def profesores(request):
    return render(request, "Appproyect/profesores.html")

def entregables(request):
    return render(request, "Appproyect/entregables.html")

def cursos(request):
    cursos = Curso.objects.all()
    return render(request, "Appproyect/cursos.html", {"cursos":cursos})






