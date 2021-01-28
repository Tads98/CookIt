from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    usuario = models.OneToOneField(
        User, on_delete=models.DO_NOTHING, verbose_name="Usuário")
