from django.urls import path
from . import views

urlpatterns = [
    path('', views.Home.home, name='home'),
    path('produto/', views.Home.produtos, name='produtos'),
    path('produto/foto/', views.Home.produtoFoto, name='produto_foto'),
]