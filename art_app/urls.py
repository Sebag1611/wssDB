from django.urls import path
from art_app.views import *

urlpatterns = [
    path('ArtRealizadas/', ArtRealizada),
    path('Arts/', obtenerArt),
    path('RiesgoCritico/', obtenerRiesgoCritico),
    path('Actividad/', obtenerActividad),
    path('RiesgoCritico/<int:id>/', modificarRiesgoCritico),
]