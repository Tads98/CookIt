from django.db import models
from PIL import Image
# Create your models here.

class Receita(models.Model):
    nome_receita = models.CharField('Nome Receita:', max_length=255, blank=False)
    modo_preparo = models.TextField('Modo de Preparo:', max_length=2000, blank=False)
    porcoes = models.IntegerField('Porções:', blank=False)
    sabor_receita = models.CharField('Sabor Receita:', max_length=100, blank=False)
    tempo_preparo = models.CharField('Tempo de Preparo:', max_length=100, blank=False)
    dono_receita = models.CharField('Dono da Receita:', max_length=100, blank=False)
    fotos = models.ImageField('Fotos', upload_to='busca/media', blank=True, null=True)
    dificuldade = models.IntegerField('Dificuldade:', blank=False)
    data_publicacao = models.DateField('data_publicacao', blank=False)

    def __str__(self):
        return self.nome_receita()

    class Meta:
        verbose_name_plural = 'Nomes Receita'