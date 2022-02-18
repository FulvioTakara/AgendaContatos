from django.contrib import admin
from .models import Contato, Categoria


@admin.register(Contato)
class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'nome', 'sobrenome', 'telefone', 'email', 'categoria', 'mostrar', )
    list_display_links = ('id', 'nome', 'sobrenome')
    list_per_page = 10
    search_fields = ('categoria', 'id', 'nome', 'sobrenome', 'data_criacao')
    list_editable = ('telefone', 'mostrar')


admin.site.register(Categoria)
