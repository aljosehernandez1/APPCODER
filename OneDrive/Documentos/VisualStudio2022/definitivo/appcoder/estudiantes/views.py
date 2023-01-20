from django.shortcuts import render, redirect
from django.urls import reverse
from django.http import HttpResponse
from datetime import datetime
from estudiantes.models import Estudiantes, Profesor, Proyecto, Curso
# Create your views here.


def saludar(request):
    return render(
        request=request,
        template_name='estudiantes/inicio.html',
    )




def listar_estudiantes(request):
    contexto ={
        'estudiantes': Estudiantes.objects.all()
        
    }
    return render(
        request=request,
        template_name='estudiantes/lista_estudiantes.html',
        context=contexto
    )

def listar_profesores(request):
    contexto ={
        'profesores': Profesor.objects.all()
        
    }
    return render(
        request=request,
        template_name='estudiantes/lista_profesores.html',
        context=contexto
    )

def listar_proyectos(request):
    contexto ={
        'proyectos': Proyecto.objects.all()
        
    }
    return render(
        request=request,
        template_name='estudiantes/lista_proyectos.html',
        context=contexto
    )

def listar_cursos(request):
    contexto ={
        'cursos': Curso.objects.all()
        
    }
    return render(
        request=request,
        template_name='estudiantes/lista_cursos.html',
        context=contexto
    )


def crear_curso(request):
    if request.method =="POST":
        data = request.POST
        curso = Curso(nombre=data['nombre'], comision=data['comision'], duracion=data['duracion'])
        curso.save()
        url_exitosa = reverse('listar_cursos')
        return redirect(url_exitosa)
    else:
        return render(
            request=request,
            template_name='estudiantes/formulario_curso.html',
        )
    
def buscar_curso(request):
    if request.method =="POST":
        data = request.POST
        cursos = Curso.objects.filter(nombre=data['nombre'])
        contexto = {
            'cursos': cursos
        }
        return render(
            request=request,
            template_name='estudiantes/lista_cursos.html',
            context=contexto,
        )
    else:
        return render(
            request=request,
            template_name='estudiantes/busqueda_curso.html',
        )