from django.db import models


class Categoria(models.Model):
    nome = models.CharField(max_length=255)

    class Meta:
        verbose_name = 'categoria'
        verbose_name_plural = 'categorias'
        ordering = ['nome']

    def __str__(self):
        return self.nome


class Contato(models.Model):
    nome = models.CharField(max_length=255)
    sobrenome = models.CharField(max_length=255, blank=True)
    telefone = models.CharField(max_length=255)
    email = models.CharField(max_length=255, blank=True, default='')
    descricao = models.TextField(blank=True)
    mostrar = models.BooleanField(default=True)
    foto = models.ImageField(blank=True, upload_to='fotos/%Y/%m')
    categoria = models.ForeignKey(Categoria, related_name='contatos',
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'contato'
        verbose_name_plural = 'contatos'
        ordering = ['nome']

    def __str__(self):
        return self.nome
