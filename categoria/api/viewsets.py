from urllib import response
from rest_framework import viewsets, status
from rest_framework.response import Response
from categoria.api import serializers
from categoria import models
from django.db.models import Avg, Count, Min, Sum
from django.db.models import Q, Value, F #Usado para realizar consultas mais complexas
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS


class CategoriaViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def categorias(self, request, pk=None):
        queryset = models.Categoria.objects.all()
        serializer_class = serializers.CategoriaSerializer(queryset, many=True)
        return Response(serializer_class.data)

    @action(detail=False, methods=['post'])
    def cadastrar(self, request):
        categoria = models.Categoria.objects.create(
            nome = request.POST.get('nome')
        )
        categoria.save()
        categoriaSalva = [
            {'id': categoria.id, 'nome': request.POST.get('nome'), 'criado_em': categoria.criado_em}
        ]
        return Response(categoriaSalva)

    @action(detail=False, methods=['post'])
    def delete(self, request):
        categoria = models.Categoria.objects.get(id=request.POST.get('id'))
        categoria.delete()
        resp = [{'msn': 'Produto deletado com sucesso', 'id': request.POST.get('id')}]
        return Response(resp)


