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
    # TODO: procurar campo ideal para por tempo
    tempo_preparo = models.PositiveIntegerField(
        'Tempo de preparo:', default=0, blank=False)
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
    quantidade = models.PositiveIntegerField(
        'Quantidade:', default=0, blank=False)

    def __str__(self):
        return self.nome_ingrediente

    class Meta:
        verbose_name_plural = 'Nomes Ingrediente'


class Usuario(models.Model):
    nome_usuario = models.CharField(
        'Nome do Usuário:', max_length=255, blank=False)

    def __str__(self):
        return self.nome_usuario

    class Meta:
        verbose_name_plural = 'Nome do Usuário'


class Avaliacao(models.Model):
    nota = models.FloatField('Nota', blank=False)
    comentario = models.TextField(
        'Comentário', max_length=200, blank=True, null=True)

    def __str__(self):
        return self.comentario

    class Meta:
        verbose_name_plural = 'Avaliações'
