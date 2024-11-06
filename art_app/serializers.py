from rest_framework import serializers
from art_app import models
from art_app.models import Art


class ARTSerializer(serializers.ModelSerializer):
    class Meta:
        model = Art
        fields = '__all'