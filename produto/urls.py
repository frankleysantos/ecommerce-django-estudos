from django.urls import path, include
from . import views

from rest_framework import routers
from produto.api import viewsets as produtoviewsets

route = routers.DefaultRouter()
route.register('', produtoviewsets.ProdutoViewSet, basename='Produtos')

urlpatterns = [
    path('cadastro/', views.index, name='produto'),
    path('detalhes/', views.detalhes, name='produto_detalhes'),
    path('api/', include(route.urls))
]