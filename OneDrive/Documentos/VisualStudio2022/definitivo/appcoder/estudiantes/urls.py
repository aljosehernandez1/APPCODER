from django.urls import path

from estudiantes.views import (saludar, listar_estudiantes, 
listar_profesores, listar_proyectos, listar_cursos, crear_curso, buscar_curso
)

urlpatterns = [
    path('saludar/', saludar),
    path('lista-alumnos/', listar_estudiantes, name="listar_alumnos"),
    path('lista-profesores/', listar_profesores, name="listar_profesores"),
    path('lista-proyectos/', listar_proyectos, name="listar_proyectos"),
    path('lista-cursos/', listar_cursos, name="listar_cursos"),
    path('crear-curso/', crear_curso, name="crear_curso"),
    path('buscar-cursos/', buscar_curso, name="buscar_curso"),     
]
