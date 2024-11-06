from django.urls import path
from art_app import views

urlpatterns = [
    path('ARTS/', views.obtener_ARTS),
]