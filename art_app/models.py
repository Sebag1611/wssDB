from django.db import models
from django.db.models import Model

from personal_app.models import Empleado

# Create your models here.
class RiesgoCritico(models.Model):
    rc_id = models.BigAutoField(primary_key=True)
    rc_nombre = models.CharField(max_length=100)
    rc_pregunta = models.CharField(max_length=200)
    rc_respuesta = models.BooleanField()

class Actividad(models.Model):
    act_id = models.BigAutoField(primary_key=True)
    act_nombre = models.CharField(max_length=100)
    act_riesgo = models.CharField(max_length=200)
    act_medida_control = models.CharField(max_length=200)

    riesgo_critico = models.ManyToManyField(RiesgoCritico)

class Pregunta(models.Model):
    pre_id = models.BigAutoField(primary_key=True)
    pre_descripcion = models.CharField(max_length=200)
    pre_cargo = models.CharField(max_length=50)
    pre_respuesta = models.BooleanField()

class Art(models.Model):
    art_id = models.BigAutoField(primary_key=True)
    art_trab_simultaneo = models.BooleanField(default=False)
    art_estado_trab = models.BooleanField(default=False)
    art_hora_inicio = models.TimeField()
    art_hora_fin = models.TimeField()
    art_fecha = models.DateField()

    pregunta = models.ManyToManyField(Pregunta, through='ArtPregunta')
    actividad = models.ManyToManyField(Actividad)
    empleado = models.ManyToManyField(Empleado)


class ArtPregunta(models.Model):
    id_art = models.ForeignKey(Art, on_delete=models.CASCADE)
    id_pregunta = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    respuesta = models.BooleanField()


