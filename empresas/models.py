from django.db import models


class Tag(models.Model):
    valor = models.CharField(max_length=255)


class Producto(models.Model):
    nombre = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.nombre}"


class ProductoTag(models.Model):
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)


class Empresa(models.Model):
    leyenda = models.CharField(max_length=255)
    razon_social = models.CharField(max_length=255)
    direccion = models.CharField(max_length=512)

    def __str__(self):
        return f"{self.leyenda} - {self.razon_social}"
