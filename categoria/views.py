from django.shortcuts import render
from django.contrib import messages

from .models import Categoria
#api
from rest_framework import viewsets
from django.http import JsonResponse 


# Create your views here.
def index(request):
    categorias = Categoria.objects.all()
    # return JsonResponse({'categorias': categorias})
    return render(request, 'categoria/index.html', {
        'categorias': categorias
    })
    