from operator import pos
from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
# from .models import Contato
from django.core.paginator import Paginator # paginação
from django.db.models import Q, Value #Usado para realizar consultas mais complexas
from django.db.models.functions import Concat # concatenação de campos
from django.contrib import messages
from django.http import JsonResponse 

# Create your views here.
def index(request):
    return render(request, 'pedido/index.html')