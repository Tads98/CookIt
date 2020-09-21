from django.db import models

# aperfeiçoar classe


class Usuario(models.Model):
    nome_usuario = models.CharField(
        'Nome do Usuário:', max_length=255, blank=False)

    def __str__(self):
        return self.nome_usuario

    class Meta:
        verbose_name_plural = 'Nome do Usuário'
