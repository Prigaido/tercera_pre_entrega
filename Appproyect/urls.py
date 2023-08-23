from django.urls import path
from .views import *

urlpatterns = [
    path('crear_curso/', crear_curso),
    path('listar_cursos/', listar_cursos),
    path('profesores/', profeformulario, name='profesores'),
    path('cursos/', cursoformulario,  name='cursos'),
    path('entregables/', entregaformulario, name='entregables'),
    path('alumnos/', alumformulario,  name='alumnos'),
]