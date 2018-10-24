from django.shortcuts import render
from .models import Estudiante, Materia, Carrera, Monitor, Horario

# Create your views here.
def home(request):
    materias = Materia.objects.order_by('nombre')
    monitores = Monitor.objects.order_by('nombre')
    info_destacados = {"materia":materias, "monitor":monitores}
    return render(request, 'edushareApp/Index.html', info_destacados)
