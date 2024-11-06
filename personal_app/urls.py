from django.urls import path
from personal_app import views

urlpatterns = [
    path('Trabajadores/', views.obtenerTrabajadores),
    path('Empleado/<int:id>', views.obtenerEmpleado),
    path('Empleado/modificar/<int:id>/<int:idEmpleado>', views.modificarEmpleado),
    path('EmpleadosCargo/<str:cargo>', views.obtenerEmpleadosCargo),
]