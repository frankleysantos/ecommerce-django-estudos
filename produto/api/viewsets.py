from pickle import FALSE
from rest_framework import viewsets, status
from rest_framework.response import Response
from produto.api import serializers
from produto import models
from django.db.models import Avg, Count, Min, Sum
from django.db.models import Q, Value, F #Usado para realizar consultas mais complexas
from produto.models import FotoProduto, Produto
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS

# class ProdutoViewSet(viewsets.ModelViewSet):
#         permission_classes = (IsAuthenticated,)
#         serializer_class = serializers.ProdutoSerializer
#         queryset = models.Produto.objects.select_related()
class ProdutoViewSet(viewsets.ViewSet):
        permission_classes = (IsAuthenticated,)

        @action(detail=False, methods=['get'])
        def lista(self, request, pk=None):
                queryset = models.Produto.objects.select_related()
                serializer_class = serializers.ProdutoSerializer(queryset, many='True')
                return Response(serializer_class.data)

        @action(detail=False, methods=['get'])
        def detalhes(self, request, pk=None):
                print(request.GET.get('id'))
                queryset = produto = Produto.objects.filter(
                        fotoproduto__produto__id=request.GET.get('id'),
                ).values('id', 'nome', 'descricao', 'categoria__nome', 'fotoproduto__foto', 'valor', 'desconto').annotate(
                        calculo=Sum(F('valor') - (F('valor') * ( F('desconto') / 100)))
                )
                # print(queryset.query)
                # serializer_class = serializers.ProdutoSerializer(queryset, many='True')
                return Response(queryset)

 

        @action(detail=False, methods=['post'])
        def inserir(self, request, pk=None):
                print(request.FILES['imagem_principal'])
                queryset =''
                if request.POST:
                        nome = request.POST.get('nome')
                        categoria_id = request.POST.get('categoria_id')
                        valor = float(request.POST.get('valor'))
                        desconto = float(request.POST.get('desconto'))
                        descricao = request.POST.get('descricao')
                        imagem_principal = request.FILES['imagem_principal'] #pega unico arquivo
                        produto = Produto.objects.create(
                                nome                    = nome,
                                categoria_id            = categoria_id,
                                valor                   = valor,
                                desconto                = desconto,
                                descricao               = descricao,
                                imagem_principal        = imagem_principal
                        )
                        produto.save()
                        form = request.FILES
                        if form:
                                fotos = request.FILES.getlist('fotos') #pegar multiplos arquivos
                                for foto in fotos:
                                        FotoProduto.objects.create(foto=foto, produto_id = produto.id)
                        queryset = {
                                'produto_id': produto.id,
                                'produto':nome
                        }
                return Response(queryset)