from django.db import models
import uuid

# Create your models here.


class Usuario(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nome = models.CharField(max_length=200)
    endereco = models.CharField(max_length=200)
