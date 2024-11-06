from django.urls import path
from art_app.views import *

urlpatterns = [
    path('Art/', obtenerArts),
    path('Art/modificar/<int:id>/', modificarArt),
    path('Art/<int:id>/', obtenerArt),
    path('RiesgoCritico/', obtenerRiesgoCriticos),
]