from rest_framework import viewsets, status
from rest_framework.response import Response
from django.db.models import Avg, Count, Min, Sum
from django.db.models import Q, Value, F #Usado para realizar consultas mais complexas
from rest_framework.decorators import action, permission_classes, api_view
from rest_framework.permissions import BasePermission, IsAuthenticated, SAFE_METHODS
from rest_framework.authtoken.models import Token


class UsuarioViewSet(viewsets.ViewSet):

    permission_classes = (IsAuthenticated,)

    @action(detail=False, methods=['get'])
    def user(self, request, format=None):
        user = {
            'username' : request.user.username,
            'first_name' : request.user.first_name,
            'last_name' : request.user.last_name,
            'email' : request.user.email,
        }
        return Response(user)

