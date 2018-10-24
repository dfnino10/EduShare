from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('reserva', views.reserva_horario, name='reserva_horario'),
    path('materia', views.materia, name='materia'),
    path('monitor', views.monitor, name='monitor'),
]