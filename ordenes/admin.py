from django.contrib import admin
from .models import OrdenCompra, CompraProductos


@admin.register(OrdenCompra)
class OrdenCompraAdmin(admin.ModelAdmin):
    # "producto"
    list_filter = ["comprador", "proveedor", "tipo_de_pago", "forma_de_pago", "camion"]
    list_display = ["fecha", "comprador", "proveedor", "importe"]

@admin.register(CompraProductos)
class CompraProductosAdmin(admin.ModelAdmin):
    pass


