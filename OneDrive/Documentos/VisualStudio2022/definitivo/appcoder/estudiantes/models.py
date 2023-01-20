from django.db import models

# Create your models here.
class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    comision = models.IntegerField()
    duracion = models.IntegerField()

class Estudiantes(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return f"{self.apellido},{self.nombre}"

    
class Profesor(models.Model):
    nombre = models.CharField(max_length=200)
    apellido = models.CharField(max_length=200)
    dni = models.CharField(max_length=200)
    email = models.EmailField()
    profesion = models.CharField(max_length=200)
    bio = models.TextField()

class Proyecto(models.Model):
    nombre = models.CharField(max_length=200)
    fecha_de_entrega = models.DateTimeField()
    aprobado = models.BooleanField(default=False)
