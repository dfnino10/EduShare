from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
import datetime

OPCIONES_CARRERA = (
    ("ADM" , 'Administración'),
    ("ANTR" , 'Antropoloía'),
    ("ARQ" , 'Arquitectura'),
    ("ART" , 'Arte'),
    ("BIO" , 'Biología'),
    ("CPOL" , 'Ciencia Política'),
    ("CONT" , 'Contaduría Internacional'),
    ("DER" , 'Derecho'),
    ("DIS" , 'Diseño'),
    ("ECON" , 'Economía'),
    ("FIL" , 'Filosofía'),
    ("FISI" , 'Física'),
    ("GEO" , 'Geociencias'),
    ("GOB" , 'Gobierno y Asuntos Públicos'),
    ("HIST" , 'Historia'),
    ("HART" , 'Historia del Arte'),
    ("IAM" , 'Ingeniería Ambiental'),
    ("IBIO" , 'Ingeniería Biomédica'),
    ("ICI" , 'Ingeniería Civil'),
    ("ISIS" , 'Ingeniería de Sistemas y Computación'),
    ("IETRI", 'Ingeniería Electrónica'),
    ("IETRO", 'Ingeniería Electrónica'),
    ("IIND", 'Ingeniería Industrial'),
    ("IMEC", 'Ingeniería Mecánica'),
    ("IQUI", 'Ingeniería Química'),
    ("LENG", 'Lenguas y Cultura'),
    ("LART", 'Licenciatura en Artes'),
    ("LCN", 'Licenciatura en Ciencias Naturales'),
    ("LCS", 'Licenciatura en Ciencias Sociales'),
    ("LCEP", 'Licenciatura en Educación para la Primera Infancia'),
    ("LH", 'Licenciatura en Humanidades'),
    ("LM", 'Licenciatura en Matemáticas'),
    ("LIT", 'Lteratura'),
    ("MAT", 'Matemáticas'),
    ("MED", 'Medicina'),
    ("MIC", 'Microbiología'),
    ("MUS", 'Música'),
    ("ND" , 'Narrativas Digitales'),
    ("PSI", 'Psicología'),
    ("QUI", 'Química'),
)
# Create your models here.

class Carrera(models.Model):
    nombre = models.CharField(max_length=100, choices=OPCIONES_CARRERA, default='')

class Materia(models.Model):
    nombre= models.CharField(max_length=50, default='')
    carrera= models.ForeignKey(Carrera, on_delete=models.CASCADE, default='')

class Categoria(models.Model):
    nombre = models.CharField(max_length = 50, default = '')
    descuento = models.FloatField(default = 0.0)

class Nivel(models.Model):
    nombre = models.CharField(max_length = 50, default = '')
    limite = models.IntegerField(default = 0)
    fee = models.FloatField(default = 0.0)
    cobromaximo = models.FloatField(default = 0.0)

class Estudiante(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, default ='')
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    imagen = models.ImageField(upload_to='imagen_perfil', blank= True)
    categoria = models.ForeignKey(Categoria, on_delete = models.SET_NULL, null = True)

class Horario(models.Model):
    fecha = models.DateField()
    hora_inicio = models.TimeField()
    hora_fin = models.TimeField()
    disponibilidad = models.BooleanField(default = False)

class Monitor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200, default='')
    carrera = models.ForeignKey(Carrera,on_delete=models.CASCADE)
    email = models.EmailField(max_length=200)
    imagen = models.ImageField(upload_to='imagen_perfil', blank=True)
    horario = models.ManyToManyField(Horario)
    nivel = models.ForeignKey(Nivel, on_delete = models.SET_NULL, null = True)

class Monitoria (models.Model):
    estudiante = models.ForeignKey(Estudiante, on_delete=models.CASCADE)
    monitor = models.ForeignKey(Monitor, on_delete=models.CASCADE)
    horario = models.ForeignKey(Horario, on_delete = models.CASCADE, default='')
    lugar = models.CharField(max_length=200, default='')
    materia = models.CharField(max_length=200, default='')
    tema = models.CharField(max_length=200, default='')