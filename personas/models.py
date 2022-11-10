from django.db import models


class Empleado(models.Model):
    nombre = models.CharField(max_length=128)
    apellido = models.CharField(max_length=128)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Camion(models.Model):
    patente = models.CharField(max_length=16, unique=True)
    numero_interno = models.CharField(max_length=12, unique=True)

    def __str__(self):
        return f"{self.patente}, Numero Interno: {self.numero_interno}"



