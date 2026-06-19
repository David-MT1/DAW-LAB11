from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ProductoViewSet, CursoViewSet, LibroViewSet, UsuarioViewSet

router = DefaultRouter()
router.register(r'productos', ProductoViewSet, basename='producto')
router.register(r'cursos', CursoViewSet, basename='curso')
router.register(r'libros', LibroViewSet, basename='libro')
router.register(r'usuarios', UsuarioViewSet, basename='usuario')

urlpatterns = [
    path('', include(router.urls)),
]