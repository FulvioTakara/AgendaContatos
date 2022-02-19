from django.urls import path
from .views import CategoriaAPIView, ContatoAPIView, \
    ContatosAPIView, CategoriasAPIView

from . import views



urlpatterns = [
    path('categorias', CategoriasAPIView.as_view(), name='categorias'),
    path('categorias/<int:pk>/', CategoriaAPIView.as_view(), name='categoria'),
    path('contatos', ContatosAPIView.as_view(), name='contatos'),
    path('contatos/<int:pk>/', ContatoAPIView.as_view(), name='contato'),

    path('busca/', views.busca, name='busca'),
]
