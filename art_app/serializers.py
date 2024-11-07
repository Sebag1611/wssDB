from rest_framework import serializers
from art_app.models import *


class ARTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = '__all__'

    def crearArt(self, validated_data):
        # Extraer datos anidados
        actividad_data = validated_data.pop('actividad')
        empleado_data = validated_data.pop('empleado')
        pregunta_data = validated_data.pop('pregunta')

        # Crear los objetos relacionados
        actividad = Actividad.objects.create(**actividad_data)
        empleado = Empleado.objects.create(**empleado_data)
        pregunta = Pregunta.objects.create(**pregunta_data)

        # Crear el objeto Art y asociarlo con los objetos creados
        art = Art.objects.create(actividad=actividad, empleado=empleado, pregunta=pregunta, **validated_data)
        return art

class RiesgoCriticoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RiesgoCritico
        fields = '__all__'

class ActividadSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actividad
        fields = '__all__'

class PreguntaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Pregunta
        fields = '__all__'