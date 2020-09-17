from django.db import models


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

    def __str__(self):
        return self.nome_receita

    class Meta:
        verbose_name_plural = 'Nomes Receita'


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
        verbose_name_plural = 'Nomes Ingrediente'


class Avaliacao(models.Model):
    nota = models.FloatField('Nota', blank=False)
    comentario = models.TextField(
        'Comentário', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.comentario

    class Meta:
        verbose_name_plural = 'Avaliações'
