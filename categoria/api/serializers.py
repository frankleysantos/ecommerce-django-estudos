from dataclasses import fields
from rest_framework import serializers
from categoria import models

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Categoria
        fields = '__all__'
