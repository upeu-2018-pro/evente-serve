from django.contrib import admin
from catalogo.models_raiz import Producto
from catalogo.models_raiz import UnidadMed
from catalogo.models.categoria import Categoria
from catalogo.models.diagnostico import Diagnostico

from catalogo.models_raiz import Venta, ShoppingCart, Cliente
# Register your models here.
admin.site.register(Diagnostico)

admin.site.register(UnidadMed)
admin.site.register(Categoria)
admin.site.register(Cliente)
admin.site.register(ShoppingCart)
admin.site.register(Venta)


class ProductoAdmin(admin.ModelAdmin):
    """docstring for ProductoAdmin"""
    list_per_page = 2
    list_display = ("codigo", "nombre",
                    "unidad_med_codigo", "categorias")
    search_fields = ("codigo", "nombre",)

    def unidad_med_codigo(self, obj):
        return obj.unidad_med.codigo

    def categorias(self, obj):
        return obj.categoria.all()

admin.site.register(Producto, ProductoAdmin)
