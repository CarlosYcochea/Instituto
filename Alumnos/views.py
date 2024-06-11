from django.shortcuts import render

from .models import Alumno,Genero

# Create your views here.
class persona:
    def __init__(self, nombre, edad):
        self.nombre=nombre
        self.edad=edad
        super().__init__()

def index(request):
    hijo=persona("juan perez","7")


    lista=["lazaña","charquican","Porotos granados"]

    alumnos= Alumno.objects.all()


    context={"hijo":hijo,"nombre":"claudia andrea","comidas":lista,"alumnos":alumnos}

    return render(request, 'alumnos/index.html', context)          