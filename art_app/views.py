from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from art_app.models import Art
from art_app.serializers import ARTSerializer

@api_view(['GET'])
def obtener_ARTS(request):
    # Utilizamos prefetch_related para las relaciones Many-to-Many
    resultados = Art.objects.prefetch_related('empleado', 'actividad').all()

    datos = []
    for resultado in resultados:
        datos.append({
            'art_id': resultado.art_id,
            'trabajo_simultaneo': resultado.art_trab_simultaneo,
            'estado_trab': resultado.art_estado_trab,
            'hora_inicio': resultado.art_hora_inicio,
            'hora_fin': resultado.art_hora_fin,
            'empleados': [{'rut': empleado.emp_rut, 'nombre': empleado.emp_nombre} for empleado in resultado.empleado.all()],
            'actividades': [{'nombre': actividad.act_nombre, 'riesgo': actividad.act_riesgo, 'medida_control': actividad.act_medida_control} for actividad in resultado.actividad.all()],
        })

    return Response(datos)