from django.contrib import admin
from .models import Tag, ProductoTag, Producto, Empresa


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

@admin.register(ProductoTag)
class ProductoTagAdmin(admin.ModelAdmin):
    pass

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    pass

@admin.register(Empresa)
class EmpresaAdmin(admin.ModelAdmin):
    pass

