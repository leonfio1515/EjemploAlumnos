from django.urls import path
from .views import *

urlpatterns = [
    path('', VInicio, name="inicio"),
    path('contacto', VContacto, name="contacto"),
    path('cursos', VCursos, name="cursos"),
    path('alumnos', VAlumnosListView.as_view(), name="alumnos"),   
    path('profesores', VProfesores, name="profesores"),
    path('inscribirse', VInscribirse, name="inscribirse"),
    path('noticias', VNoticias, name="noticias"),
    path('buscar', VBuscar, name="buscar"),


]
