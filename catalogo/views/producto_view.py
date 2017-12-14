from ..models_raiz import Producto
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce

from core.pagination import ModelPagination


class ProductoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Producto
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class ProductoViewSet(ModelPagination, viewsets.ModelViewSet):
    queryset = Producto.objects.all()
    serializer_class = ProductoSerializer
    #permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        query = self.request.query_params.get('query', '')
        queryall = (Q(codigo__icontains=query),
                    Q(nombre__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
