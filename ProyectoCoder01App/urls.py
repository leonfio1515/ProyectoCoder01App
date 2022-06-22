from django.urls import path
from .views import *

urlpatterns = [
    path('', VInicio, name="inicio"),
    path('contacto', VContacto, name="contacto"),
    path('cursos', VCursos, name="cursos"),
    path('alumnos', VAlumnos, name="alumnos"),   
    path('profesores', VProfesores, name="profesores"),
    path('inscribirse', VInscribirse, name="inscribirse"),
    path('noticias', VNoticias, name="noticias"),


]
