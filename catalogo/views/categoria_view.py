from ..models.categoria import Categoria
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce
import logging
log = logging.getLogger(__name__)


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        log.info('Writing in log file', extra={
            'path': self.request.get_full_path(),
            'ip': self.request.META['REMOTE_ADDR'],
            'user': self.request.user,
            'method': self.request.method
        })
        query = self.request.query_params.get('query', '')
        queryall = (Q(codigo__icontains=query),
                    Q(nombre__icontains=query))
        queryset = self.queryset.filter(reduce(OR, queryall))
        return queryset
