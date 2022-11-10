from django.db import models
from personas.models import Empleado, Camion
from empresas.models import Empresa, Producto
from django.utils.translation import gettext_lazy as _


class OrdenCompra(models.Model):
    class TipoDePagos(models.TextChoices):
        REGISTRADO = 'RG', _('Registrado')
        NO_REGISTRADO = 'NRG', _('No Registrado')

    class FormaDePago(models.TextChoices):
        EFECTIVO = 'EFECTIVO', _('Efectivo')
        CHEQUE = 'CHEQUE', _('Cheque')
        TRANSFERENCIA = 'TRANSFERENCIA', _('Transferencia')
        CREDITO = 'CREDITO', _('Credito')
        DEBITO = 'DEBITO', _('Debito')

    fecha = models.DateTimeField()
    n_orden = models.PositiveIntegerField()
    comprador = models.ForeignKey(Empleado, on_delete=models.SET_NULL, null=True)
    proveedor = models.ForeignKey(Empresa, on_delete=models.SET_NULL, null=True)
    numero_de_factura = models.PositiveIntegerField()
    tipo_de_pago = models.CharField(max_length=3, choices=TipoDePagos.choices)
    forma_de_pago = models.CharField(max_length=32, choices=FormaDePago.choices)
    camion = models.ForeignKey(Camion, on_delete=models.SET_NULL, null=True)
    importe = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.n_orden}"


class CompraProductos(models.Model):
    orden_de_compra = models.ForeignKey(OrdenCompra, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return f"Se compro {self.producto} en esta orden de compra {self.orden_de_compra}"

