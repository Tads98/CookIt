from django.db import models


class Receita(models.Model):
    nome_receita = models.CharField(
        'Nome Receita:', max_length=255, blank=False)
    modo_preparo = models.TextField(
        'Modo de Preparo:', max_length=2000, blank=False)
    porcoes = models.IntegerField('Porções:', blank=False)
    sabor_receita = models.CharField(
        'Sabor Receita:', max_length=100, blank=False)
    tempo_preparo = models.CharField(
        'Tempo de Preparo:', max_length=100, blank=False)
    dono_receita = models.CharField(
        'Dono da Receita:', max_length=100, blank=False)
    # fotos = models.ImageField(
    #    'Fotos', upload_to='busca/media', blank=True, null=True)
    dificuldade = models.IntegerField('Dificuldade:', blank=False)
    data_publicacao = models.DateField('data_publicacao', blank=False)

    def __str__(self):
        return self.nome_receita()

    class Meta:
        verbose_name_plural = 'Nomes Receita'


class Ingrediente(models.Model):
    receita = models.ForeignKey(Receita, on_delete=models.DO_NOTHING)
    nome_ingrediente = models.CharField(
        'Nome Ingrediente:', max_length=100, blank=False)
    quantidade = models.FloatField('Quantidade:', default=0, blank=False)

    def __str__(self):
        return self.nome_ingrediente()

    class Meta:
        verbose_name_plural = 'Nomes Ingrediente'


class Usuario(models.Model):
    nome_usuario = models.CharField(
        'Nome do Usuário:', max_length=255, blank=False)

    def __str__(self):
        return self.nome_usuario()

    class Meta:
        verbose_name_plural = 'Nome do Usuário'
