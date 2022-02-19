from rest_framework import generics
from .models import Contato, Categoria
from .Serializers import CategoriaSerializer, ContatoSerializer



class CategoriasAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ContatosAPIView(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer


class ContatoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
