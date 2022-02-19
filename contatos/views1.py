from django.shortcuts import render, get_object_or_404
from django.http import Http404
from .models import Contato
from django.core.paginator import Paginator
from django.contrib import messages
from django.db.models import Q, Value
from django.db.models.functions import Concat

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Contato, Categoria
from .Serializers import ContatoSerializer, CategoriaSerializer


def index(request):
    messages.add_message(request,messages.ERROR, 'Ocorreu um erro')

    contatos = Contato.objects.order_by('nome').filter(
        mostrar=True
    )
    paginator = Paginator(contatos, 20)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/index.html', {
         'contatos': contatos
    })

def ver_contato(request, contato_id):
    contato = get_object_or_404(Contato, id=contato_id)

    if not contato.mostrar:
        raise Http404()

    return render(request, 'contatos/ver_contato.html', {
         'contato': contato
    })

def busca(request):
    termo = request.GET.get('termo')

    if termo is None or not termo:
        return Http404()

    campos = Concat('nome', Value(' '),  'sobrenome')

    contatos = Contato.objects.annotate(
        nome_completo=campos
    ).filter(
        Q(nome_completo__icontains=termo) | Q(
            categoria__icontains=termo
        )
    )
    paginator = Paginator(contatos, 10)

    page = request.GET.get('p')
    contatos = paginator.get_page(page)

    return render(request, 'contatos/busca.html', {
         'contatos': contatos
    })

# API_REST
class CategoriaAPIView(APIView):
    def get(self, request):
        categorias = Categoria.objects.all()
        serializer = CategoriaSerializer(categorias, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = CategoriaSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class ContatoAPIView(APIView):
    def get(self, request):
        contatos = Contato.objects.all()
        serializer = ContatoSerializer(contatos, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = ContatoSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)