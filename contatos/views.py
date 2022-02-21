from rest_framework import generics
from rest_framework.generics import get_object_or_404

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Contato, Categoria
from .Serializers import CategoriaSerializer, ContatoSerializer

# API Versão 1
class CategoriasAPIView(generics.ListCreateAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class CategoriaAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer


class ContatosAPIView(generics.ListCreateAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

    def get_queryset(self):
        if self.kwargs.get('categoria_pk'):
            return self.queryset.filter(categoria_id=self.kwargs.get('categoria_pk'))
        return self.queryset.all()


class ContatoAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer

    def get_object(self):
        if self.kwargs.get('categoria_pk'):
            return get_object_or_404(self.get_queryset(),
                                     categoria_id=self.kwargs.get('categoria_id'),
                                     pk=self.kwargs.get('contato_pk'))
        return get_object_or_404(self.get_queryset(), pk=self.kwargs.get('contato_pk'))

# API Versão 2


class CategoriaViewSet(viewsets.ModelViewSet):
    queryset = Categoria.objects.all()
    serializer_class = CategoriaSerializer

    @action(detail=True, methods=['get'])
    def contatos(self, request, pk=None):
        categoria = self.get_object()
        serializer = ContatoSerializer(categoria.contatos.all(), many=True)
        return Response(serializer.data)


class ContatoViewSet(viewsets.ModelViewSet):
    queryset = Contato.objects.all()
    serializer_class = ContatoSerializer
