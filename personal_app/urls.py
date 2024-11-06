from django.urls import path
from personal_app import views

urlpatterns = [
    path('Empleados/', views.obtenerEmpleados),
    path('Empleado/<int:id>', views.Empleado),
    path('Empleado/modificar/<int:id>', views.modificarEmpleado),
]