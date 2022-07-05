from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# from .models import Contato
from django.core.paginator import Paginator # paginação
from django.db.models import Q, Value, F #Usado para realizar consultas mais complexas
from django.db.models.functions import Concat # concatenação de campos
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Count
from produto import models
from pymysql import NULL
from django.db.models import Avg, Count, Min, Sum
from produto.api import serializers
from rest_framework.permissions import IsAuthenticated

from categoria.models import Categoria
from produto.models import FotoProduto, Produto
# Create your views here.
def index(request):
    categorias = Categoria.objects.all()
    if request.POST:
        nome = request.POST.get('nome')
        categoria_id = request.POST.get('categoria_id')
        descricao = request.POST.get('descricao')
        produto = Produto.objects.create(
            nome            = nome,
            categoria_id    = categoria_id,
            descricao       = descricao
        )
        produto.save()
        form = request.FILES
        if form:
            fotos = request.FILES.getlist('fotos')
            for foto in fotos:
                FotoProduto.objects.create(foto=foto, produto_id = produto.id)
       
        
    return render(request, 'produto/index.html', {
        'categorias': categorias
    })

def detalhes(request):
    try:
        if (request.GET.get('id')):
            produto = Produto.objects.filter(
                fotoproduto__produto__id=request.GET.get('id'),
            ).values('id', 'nome', 'descricao', 'categoria__nome', 'fotoproduto__foto', 'valor', 'desconto').annotate(
                calculo=Sum(F('valor') - (F('valor') * ( F('desconto') / 100)))
             )
            print(produto.query)
            #listProduto = [lista for lista in produto] #converte para lista

            return render(request, 'produto/detalhes.html', {
                'produto': produto
            })
    except Exception as e:
        print("Oops!", e.__class__, "occurred.")
        return redirect('home')