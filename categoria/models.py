from django.db import models
from django.utils import timezone
# Create your models here.
class Categoria(models.Model):
    nome = models.CharField(max_length=255)
    criado_em = models.DateTimeField(default=timezone.now)
    def __str__(self):
        return self.nome