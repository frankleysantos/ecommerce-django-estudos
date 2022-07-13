from django.urls import path, include
from . import views
from rest_framework import routers
from accounts.api import viewsets as usuarioviewset
route = routers.DefaultRouter()
route.register('', usuarioviewset.UsuarioViewSet, basename='Usuario')

urlpatterns = [
    path('', views.login, name='login'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('api/', include(route.urls))
]