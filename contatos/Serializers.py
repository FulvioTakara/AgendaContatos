from rest_framework import serializers

from .models import Contato, Categoria


class CategoriaSerializer(serializers.ModelSerializer):

    class Meta:
        model = Categoria
        fields = ('id', 'nome',)


class ContatoSerializer(serializers.ModelSerializer):

    class Meta:

        extra_kwargs = {
            'email': {'write_only':True},
            'telefone': {'write_only':True},
        }

        model = Contato
        fields = (
            'id',
            'nome',
            'sobrenome',
            'telefone',
            'email',
            'descricao',
            'mostrar',
            'foto',
            'categoria',
        )
