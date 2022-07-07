from django.urls import path, include
from . import views

from rest_framework import routers
from categoria.api import viewsets as categoriaviewsets

route = routers.DefaultRouter()
route.register('', categoriaviewsets.CategoriaViewSet, basename='Categorias')

urlpatterns = [
    path('', views.index, name='categoria'),
    path('api/', include(route.urls))
]