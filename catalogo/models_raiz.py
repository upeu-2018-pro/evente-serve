from django.db import models
from core.models import User, Person
from .models.categoria import Categoria
# Create your models here.


class UnidadMed(models.Model):

    codigo = models.CharField(max_length=10)
    nombre = models.CharField(max_length=60, null=True, blank=True)

    class Meta:
        verbose_name = "UnidadMed"
        verbose_name_plural = "UnidadMeds"

    def __str__(self):
        return '%s (%s)' % (self.codigo, self.nombre)


class Producto(models.Model):

    nombre = models.CharField(max_length=60)
    codigo = models.CharField(max_length=10, null=True, blank=True)
    detalle = models.TextField(null=True, blank=True)
    precio_venta = models.FloatField(default=0.0)
    unidad_med = models.ForeignKey(UnidadMed, on_delete=models.CASCADE)
    categoria = models.ManyToManyField(
        "Categoria",
        verbose_name="list of Categorias")

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"

    def __str__(self):
        return '%s (%s)' % (self.nombre, self.codigo)


class Cliente(models.Model):

    ruc = models.CharField(max_length=11)
    person = models.OneToOneField(Person, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Cliente"
        verbose_name_plural = "Clientes"

    def __str__(self):
        return '%s' % (self.ruc)


class Venta(models.Model):

    nro_doc = models.CharField(max_length=15)
    fecha = models.DateTimeField(auto_now_add=True)
    total = models.FloatField(default=0)
    vendedor = models.ForeignKey(User, on_delete=models.CASCADE)
    cliente = models.ForeignKey(
        Cliente, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name = "Venta"
        verbose_name_plural = "Ventas"

    def __str__(self):
        return '%s' % (self.nro_doc)


class ShoppingCart(models.Model):

    cantidad = models.IntegerField()
    precio_uni = models.FloatField(default=0)

    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)
    venta = models.ForeignKey(Venta, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "ShoppingCart"
        verbose_name_plural = "ShoppingCarts"

    def __str__(self):
        return 'VENTA%s - PROD: %s' % (self.venta.nro_doc,
                                       self.producto.nombre,)
