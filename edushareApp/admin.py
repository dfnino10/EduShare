from django.contrib import admin
from .models import Estudiante, Materia, Carrera, Monitor, Horario


# Register your models here.
admin.site.register(Estudiante)
admin.site.register(Materia)
admin.site.register(Carrera)
admin.site.register(Monitor)
admin.site.register(Horario)