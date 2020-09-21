from django.db import models
from django.conf import settings
import os
from PIL import Image


class Receita(models.Model):
    nome_receita = models.CharField(
        'Nome Receita:', max_length=255)
    modo_preparo = models.TextField(
        'Modo de Preparo:', max_length=2000)
    porcoes = models.PositiveIntegerField('Porções:')
    sabor_receita = models.CharField(
        default='D',
        max_length=1,
        # opções do select menu
        choices=(
            ('D', 'Doce'),
            ('S', 'Salgada'),
        )
    )
    # TODO: procurar formas de inserir dias, horas e minutos ao mesmo tempo
    tempo_preparo = models.PositiveIntegerField(
        'Tempo de preparo:', default=0, blank=False)
    # variaçãoes de 'tempo_preparo'
    tempo_unidade_medida = models.CharField(
        default='M',
        max_length=1,
        # opções do select menu
        choices=(
            ('M', 'Minuto'),
            ('H', 'Hora'),
            ('D', 'Dias'),
        )
    )
    # TODO: discutir existência desta variavel neste model
    dono_receita = models.CharField(
        'Dono da Receita:', max_length=100)
    fotos = models.ImageField(
        'Fotos', upload_to='receita/media', blank=True, null=True)

    dificuldade = models.CharField(
        default='F',
        max_length=1,
        # opções do select menu
        choices=(
            ('F', 'Fácil'),
            ('M', 'Médio'),
            ('D', 'Difícil'),
            ('C', 'Master Chef'),

        )
    )
    data_publicacao = models.DateField('data_publicacao', blank=False)

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
        print('Tamanho da imagem atualizada:', Image.open(img_full_path).size)

    # metodo para redimencionar imagens ao dar upload e chamar o método de redemencionar imagens
    # no momento em que recebe o último upload
    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        max_image_size = 800

        # chamando função para redemencionar imagem
        if self.fotos:
            self.resize_image(self.fotos, max_image_size)
    #################### Redimensionar imagem FIM ######################

    def __str__(self):
        return self.nome_receita

    class Meta:
        verbose_name_plural = 'Receita'


class Ingrediente(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.DO_NOTHING)
    nome_ingrediente = models.CharField(
        'Nome Ingrediente:', max_length=100, blank=False)

    unidadeMedida = models.CharField(
        default='U',
        max_length=1,
        # opções do select menu
        choices=(
            ('U', 'Unidade'),
            ('X', 'Xícara'),
            ('C', 'Colher de Sopa'),
            ('D', 'Dente de Alho'),
            ('M', 'ML'),
            ('L', 'Litros'),

        )
    )
    quantidade = models.PositiveIntegerField(
        'Quantidade:', default=0, blank=False)

    def __str__(self):
        return self.nome_ingrediente

    class Meta:
        verbose_name_plural = 'Ingredientes'


class Avaliacao(models.Model):
    nota = models.FloatField('Nota', blank=False)
    comentario = models.TextField(
        'Comentário', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.comentario

    class Meta:
        verbose_name_plural = 'Avaliações'
