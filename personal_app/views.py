from django.shortcuts import render
from personal_app.models import Empleado
from art_app.models import *
from personal_app.serializers import *
from art_app.serializers import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view

# Create your views here.


