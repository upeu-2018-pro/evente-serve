
from django.conf.urls import url, include
from rest_framework import routers
from .views.diagnostico_view import DiagnosticoViewSet

from .views.categoria_view import CategoriaViewSet
from .views.producto_view import ProductoViewSet

router = routers.DefaultRouter()
router.register(r'diagnosticos', DiagnosticoViewSet)
router.register(r'productos', ProductoViewSet)
router.register(r'categorias', CategoriaViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
