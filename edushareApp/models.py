from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

# Create your models here.
class Estudiante(models.Model):
    user = models.OneToOneField(User)
    nombre = models.CharField(max_length=200, default ='')
    carrera = models.CharField(max_length=100, default='')
    email = models.EmailField(max_length=200)
    imagen = models.ImageField(upload_to='imagen_perfil', blank= True)


