from distutils.command.upload import upload
from tokenize import blank_re
from django.utils import timezone
from django.db import models

from categoria.models import Categoria

def upload_image_book(instace, filename):
    return f"{instace.id}-{filename}"


# Create your models here.
class Produto(models.Model):
    categoria = models.ForeignKey(Categoria, on_delete=models.DO_NOTHING, blank=True)
    nome = models.CharField(max_length=255)
    valor = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)
    desconto = models.DecimalField(max_digits=20,decimal_places=2, default=0.00)
    descricao = models.TextField(blank=True)
    criado_em = models.DateTimeField(default=timezone.now)
    imagem_principal = models.ImageField(upload_to=upload_image_book, blank=True, null=True)
    def __str__(self):
       return self.nome

class FotoProduto(models.Model):
    foto = models.FileField(upload_to='produtos')
    produto = models.ForeignKey(Produto, on_delete=models.DO_NOTHING)
    def __str__(self):
       return self.foto
