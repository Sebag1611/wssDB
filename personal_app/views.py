from django.shortcuts import render
from django.http import HttpResponse
from personal_app.models import Empleado
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import status
from personal_app.serializers import PersonalSerializer

# Create your views here.

@api_view(['GET'])
def obtenerEmpleado(request,id):
    persona = Empleado.objects.get(emp_rut =id)
    try:
        perfil = Empleado.objects.get(emp_rut=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializado = PersonalSerializer(persona)
    return Response(serializado.data)


@api_view(['GET','POST'])
def obtenerEmpleados(request):
    if request.method == 'GET':
        personas_obtenidas = Empleado.objects.all()
        serialzado = PersonalSerializer(personas_obtenidas, many=True)
        return Response(serialzado.data,status=status.HTTP_200_OK)

    if request.method == 'POST':
        deserializado = PersonalSerializer(data=request.data)

        if deserializado.is_valid():
            deserializado.save()
            return Response(deserializado.data,status=status.HTTP_200_OK)
        else:
            return Response(deserializado.errors,status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PATCH', 'DELETE'])
def modificarEmpleado(request, id, idEmpleado):
    try:
        persona = Empleado.objects.get(emp_rut=id)
        if persona.emp_cargo == "JefeLab":
            empleado = Empleado.objects.get(emp_rut=idEmpleado)
        else:
            return Response({"detail": "No tiene permisos para modificar."}, status=status.HTTP_403_FORBIDDEN)

    except Empleado.DoesNotExist:
        return Response({"detail": "Empleado no encontrado."}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializado = PersonalSerializer(empleado, data=request.data)
        if serializado.is_valid():
            serializado.save()
            return Response(serializado.data, status=status.HTTP_200_OK)
        return Response(serializado.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "DELETE":
        empleado.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)