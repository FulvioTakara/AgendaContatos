from django.urls import path
from .views import CategoriaAPIView, ContatoAPIView

from . import views



urlpatterns = [
    path('categoria', CategoriaAPIView.as_view(), name='categoria'),
    path('contatos', ContatoAPIView.as_view(), name='contatos'),
    path('<int:contato_id>', views.ver_contato, name='ver_contato'),
    path('busca/', views.busca, name='busca'),
]
