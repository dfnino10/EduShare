from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime


OPCIONES_CARRERA = {
    'ADM' : 'Administración',
    'ANTR' : 'Antropoloía',
    'ARQ' : 'Arquitectura',
    'ART' : 'Arte',
    'BIO' : 'Biología',
    'CPOL' : 'Ciencia Política',
    'CONT' : 'Contaduría Internacional',
    'DER' : 'Derecho',
    'DIS' : 'Diseño',
    'ECON' : 'Economía',
    'FIL' : 'Filosofía',
    'FISI' : 'Física',
    'GEO' : 'Geociencias',
    'GOB' : 'Gobierno y Asuntos Públicos',
    'HIST' : 'Historia',
    'HART' : 'Historia del Arte',
    'IAM' : 'Ingeniería Ambiental',
    'IBIO' : 'Ingeniería Biomédica',
    'ICI' : 'Ingeniería Civil',
    'ISIS' : 'Ingeniería de Sistemas y Computación',
    'IETRI': 'Ingeniería Electrónica',
    'IETRO': 'Ingeniería Electrónica',
    'IIND': 'Ingeniería Industrial',
    'IMEC': 'Ingeniería Mecánica',
    'IQUI': 'Ingeniería Química',
    'LENG': 'Lenguas y Cultura',
    'LART': 'Licenciatura en Artes',
    'LCN': 'Licenciatura en Ciencias Naturales',
    'LCS': 'Licenciatura en Ciencias Sociales',
    'LCEP': 'Licenciatura en Educación para la Primera Infancia',
    'LH': 'Licenciatura en Humanidades',
    'LM': 'Licenciatura en Matemáticas',
    'LIT': 'Lteratura',
    'MAT': 'Matemáticas',
    'MED': 'Medicina',
    'MIC': 'Microbiología',
    'MUS': 'Música',
    'ND' : 'Narrativas Digitales',
    'PSI': 'Psicología',
    'QUI': 'Química',
}
# Create your models here.
class Materia(models.Model):
    nombre= nombre = models.CharField(max_length=10, default='')

class Carrera(models.Model):
    nombre = models.CharField(max_length=10, choices=OPCIONES_CARRERA, default='')
    materias = models.ManyToManyField(Materia)

class Estudiante(models.Model):
    user = models.OneToOneField(User)
    nombre = models.CharField(max_length=200, default ='')
    carrera = models.ForeignKey(Carrera)
    email = models.EmailField(max_length=200)
    imagen = models.ImageField(upload_to='imagen_perfil', blank= True)


class Horario(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_inicio = models.TimeField()

class Monitor(models.Model):
    user = models.OneToOneField(User)
    nombre = models.CharField(max_length=200, default='')
    carrera = models.CharField(max_length=10, choices=OPCIONES_CARRERA, default='')
    email = models.EmailField(max_length=200)
    imagen = models.ImageField(upload_to='imagen_perfil', blank=True)
    disponibilidad = models.ManyToManyField(Horario)

class monitoria (models.Model):
    estiduante = models.ForeignKey(Estudiante)
    monitor = models.ForeignKey(Monitor)
    lugar = models.CharField(max_length=200, default='')
    materia = models.CharField(max_length=200, default='')
    materia = models.CharField(max_length=200, default='')
    tema = models.CharField(max_length=200, default='')






