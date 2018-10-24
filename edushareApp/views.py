from django.shortcuts import render
from .models import Estudiante, Materia, Carrera, Monitor, Horario

# Create your views here.
def home(request):
   return render(request, 'index.html', {})

def login(request):
    return render(request, 'LogIn.html', {})

def reserva_horario(request):
    return render(request, 'ReservarHorario.html', {})

def materia(request):
    return render(request, 'Materia.html', {})

def monitor(request):
    return render(request, 'Monitor.html', {})

