from ..models.diagnostico import Diagnostico
from rest_framework import serializers, viewsets
from rest_framework import permissions
from django.db.models import Q
from operator import __or__ as OR
from functools import reduce


class DiagnosticoSerializer(serializers.ModelSerializer):

    class Meta:
        model = Diagnostico
        fields = '__all__'
        #fields = ('id', 'username', 'email', 'is_staff')


class DiagnosticoViewSet(viewsets.ModelViewSet):
    queryset = Diagnostico.objects.all()
    serializer_class = DiagnosticoSerializer
    #permission_classes = [permissions.IsAuthenticated]
