from dataclasses import fields
from pyexpat import model
from rest_framework import serializers
# from ..models import Categoria
from categoria import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = 'nome', 'criado_em'
        # fields = '__all__'