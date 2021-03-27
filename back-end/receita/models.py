from django.db import models
from django.conf import settings
from django.contrib.auth.models import User
from django_extensions.db.fields import AutoSlugField
import os
from PIL import Image


class Ingrediente(models.Model):
    nome_ingrediente = models.CharField(
        'Nome Ingrediente:', max_length=100, blank=False)
    unidade_medida_ingrediente = models.CharField(
        default='U',
        max_length=3,
        choices=(
            ('U', 'Unidade'),
            ('X', 'Xícara'),
            ('C', 'Colher de Sopa'),
            ('CH', 'Colher de Chá'),
            ('D', 'Dente de Alho'),
            ('M', 'Mililitro(ml)'),
            ('L', 'Litros'),
            ('G', 'Gramas(g)'),
            ('KG', 'Quilograma(kg)'),
            ('AGS', 'ao gosto'),
        )
    )
    quantidade_ingrediente = models.PositiveIntegerField(
        'Quantidade:', default=0, blank=False)

    def __str__(self):
        return self.nome_ingrediente

    class Meta:
        verbose_name_plural = 'Ingredientes'
# TODO: resolver relacionamento de usuario


class Receita(models.Model):
    nome_receita = models.CharField('Nome Receita:', max_length=255)
    modo_preparo = models.TextField('Modo de Preparo:', max_length=2000)
    porcoes = models.PositiveIntegerField('Porções:')
    sabor_receita = models.CharField(
        default='D',
        max_length=1,
        choices=(
            ('D', 'Doce'),
            ('S', 'Salgada'),
        )
    )
    tempo_preparo = models.PositiveIntegerField(
        'Tempo de preparo:', default=0, blank=False)
    tempo_unidade_medida = models.CharField(
        default='M',
        max_length=1,
        choices=(
            ('M', 'Minuto'),
            ('H', 'Hora'),
            ('D', 'Dias'),
        )
    )
    dono_receita = models.ForeignKey(User, on_delete=models.CASCADE,)
    
    # TODO: configurar este model para receber somente imagens
    fotos = models.ImageField(upload_to='receita/media', blank=True, null=True)
    categoria = models.CharField(
        default='A',
        max_length=2,
        choices=(
            ('C', 'Café da manhã'),
            ('A', 'Almoço'),
            ('L', 'Lanche'),
            ('J', 'Janta'),
            ('S', 'Sobremesas'),
            ('B', 'Bebidas'),
            ('V', 'Vegana'),
        )
    )
    dificuldade = models.CharField(
        default='F',
        max_length=1,
        choices=(
            ('F', 'Fácil'),
            ('M', 'Médio'),
            ('D', 'Difícil'),
            ('C', 'Master Chef'),

        )
    )
    data_publicacao = models.DateTimeField(auto_now_add=True)
    slug = AutoSlugField(populate_from='nome_receita', default='SOME STRING')

    def slugify_function(self, content):
        return content.replace(' ', '-').lower()

    observacoes_adicionais = models.TextField(
        'Observações adicionais:', max_length=800)

    ingredientes = models.ManyToManyField(Ingrediente)

    #################### Redimensionar imagem ######################

    @staticmethod
    def resize_image(img, new_widht=800):
        # caminho completo da imagem
        img_full_path = os.path.join(settings.MEDIA_ROOT, img.name)

        # abrir a imagem usando o Image(que foi importado)
        img_pil = Image.open(img_full_path)

        # tamanho original da imagem (img_pill.size retorna dois valores: largura e altura)
        original_width, original_height = img_pil.size

        if original_width <= new_widht:
            img_pil.close()
            # termina a função se a largura original for menor que a nova largura
            return

        new_height = round((new_widht * original_height) / original_width)
        # 'Image.LANCZOS' é cálculo matemático que diminui a imagem de fato em PIXELS
        # redemencionando de fato a imagem de acordo com os parâmentros calculado acima
        new_img = img_pil.resize((new_widht, new_height), Image.LANCZOS)
        new_img.save(
            # caminho onde a imagem redemensionada deve sobrescrever a imagem antiga
            img_full_path,

            optimize=True,
            # qualidade da imagem
            quality=50
        )

    # metodo para redimencionar imagens ao dar upload e chamar o método de redemencionar imagens
    # no momento em que recebe o último upload
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        # chamando função para redemencionar imagem
        max_image_size = 800
        if self.fotos:
            self.resize_image(self.fotos, max_image_size)

    def __str__(self):
        return self.nome_receita

    class Meta:
        verbose_name_plural = 'Receita'


class Avaliacao(models.Model):
    nota = models.FloatField('Nota', blank=False)
    comentario = models.TextField(
        'Comentário', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.comentario

    class Meta:
        verbose_name_plural = 'Avaliações'
