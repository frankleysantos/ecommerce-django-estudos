from dataclasses import fields
from rest_framework import serializers
# from ..models import Categoria
from produto import models

class FotoProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.FotoProduto
        #fields = 'nome', 'criado_em'
        fields = '__all__'

class ProdutoSerializer(serializers.ModelSerializer):
    items = FotoProdutoSerializer(many=True, read_only=True)
    class Meta:
        model = models.Produto
        #fields = 'nome', 'criado_em'
        fields = '__all__'