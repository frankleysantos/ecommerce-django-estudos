from ast import IsNot
import json
from json import encoder
from operator import pos
from pickle import FALSE
from django.http import Http404, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
# from .models import Contato
from django.core.paginator import Paginator # paginação
from django.db.models import Q, Value #Usado para realizar consultas mais complexas
from django.db.models.functions import Concat # concatenação de campos
from django.contrib import messages
from django.http import JsonResponse
from django.db.models import Count
from django.contrib.auth.decorators import login_required

from produto.models import FotoProduto, Produto




# Create your views here home.
class Home():
    @login_required(redirect_field_name='')
    def home(request):
        return render(request, 'home/home.html')

    @login_required(redirect_field_name='')
    def produtos(request):
        produtos = Produto.objects.filter(
            fotoproduto__produto__isnull=False,
            categoria__produto__isnull=False
        ).annotate(total_count=Count('id')).values('id', 'nome', 'descricao', 'categoria__nome')
        return JsonResponse({"produtos": list(produtos)})

    def produtoFoto(request):
        if request.GET.get('id'):
            id = request.GET.get('id')
            foto = FotoProduto.objects.filter(produto_id=id)[:1].all()
            for ft in foto:
                foto = (f'{ft.foto}')

            return JsonResponse({'foto': foto})
        