from django.shortcuts import render
from personal_app.models import Empleado
from art_app.models import *
from personal_app.serializers import *
from art_app.serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.
# Obtener y añadir Art a la base de datos
@api_view(['GET', 'POST'])
def obtenerArts(request):
    if request.method == 'GET':
        art_obtenida = Art.objects.all()
        #serializar los resultados
        serializado = ArtSerializer(art_obtenida, many=True)
        return Response(serializado.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        deserializado = ArtSerializer(data=request.data)
        # Valida q el JSON recibido es correcto segun la bd
        if deserializado.is_valid():
            # Graba el resultado en la bd
            deserializado.save()
            return Response(deserializado.data, status=status.HTTP_200_OK)
        else:
            # En caso de errores, devuelve los errores
            return Response(deserializado.errors, status=status.HTTP_400_BAD_REQUEST)

def obtenerRiesgoCriticos(request):
    if request.method == 'GET':
        rc_obtenido = RiesgoCritico.objects.all()
        serializado = RiesgoCriticoSerializer(rc_obtenido, many=True)
        return Response(serializado.data, status=status.HTTP_200_OK)

    if request.method == 'POST':
        deserializado = RiesgoCriticoSerializer(data=request.data)
        if deserializado.is_valid():
            deserializado.save()
            return Response(deserializado.data, status=status.HTTP_200_OK)


@api_view(['PATCH', 'DELETE'])
def modificarArt(request, id):
    try:
        art = Art.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PATCH':
        serializer = ArtSerializer(art, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == 'DELETE':
        art.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['GET'])
def obtenerArt(request, id):
    try:
        art = Art.objects.get(id=id)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = ArtSerializer(art)
        return Response(serializer.data, status=status.HTTP_200_OK)
