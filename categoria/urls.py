from django.urls import path, include
from . import views

from rest_framework import routers
route = routers.DefaultRouter()

urlpatterns = [
    path('', views.index, name='categoria'),
    # path('api/categorias', views.apiCategorias, name='api_categorias'),
]