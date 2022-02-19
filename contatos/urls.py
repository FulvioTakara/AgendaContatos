from django.urls import path

from rest_framework.routers import SimpleRouter

from .views import (
    CategoriaAPIView,
    ContatoAPIView,
    ContatosAPIView,
    CategoriasAPIView,
    ContatoViewSet,
    CategoriaViewSet,
)


router = SimpleRouter()
router.register('categorias', CategoriaViewSet)
router.register('contatos', ContatoViewSet)


urlpatterns = [
    path('categorias', CategoriasAPIView.as_view(), name='categorias'),
    path('categorias/<int:pk>/', CategoriaAPIView.as_view(), name='categoria'),
    path('categorias/<int:categoria_pk>/contatos/', ContatosAPIView.as_view(), name='categoria_contatos'),
    path('categorias/<int:categoria_pk>/contatos/<int:contato_pk>/',
         ContatoAPIView.as_view(), name='categoria_contato'),

    path('contatos', ContatosAPIView.as_view(), name='contatos'),
    path('contatos/<int:contato_pk>/', ContatoAPIView.as_view(), name='contato'),
]

"""

from . import views
path('busca/', views.busca, name='busca'),
"""
