from django.contrib import admin
from .models import Empleado, Camion


@admin.register(Empleado)
class EmpleadoAdmin(admin.ModelAdmin):
    pass

@admin.register(Camion)
class CamionAdmin(admin.ModelAdmin):
    pass