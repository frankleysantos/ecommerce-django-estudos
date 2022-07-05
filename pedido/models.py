from django.db import models
from django.utils import timezone

# Create your models here.
class Pedido(models.Model):
    data_pedido = models.DateTimeField(default=timezone.now)