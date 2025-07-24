from django.contrib.auth.models import User
from django.db import models

class Fofoca(models.Model):
    class Bairro(models.TextChoices):
        CENTRO = "CENTRO", "Centro"
        AQUARIUS = "AQUARIUS", "Jardim Aquarius"
        SATELITE = "SATELITE", "Jardim Satélite"
        URBANOVA = "URBANOVA", "Urbanova"
        VILA_EMA = "VILA_EMA", "Vila Ema"
        BOSQUE = "BOSQUE", "Bosque dos Eucaliptos"
        ESPLANADA = "ESPLANADA", "Jardim Esplanada"
        PARQUE_INDUSTRIAL = "PARQUE_INDUSTRIAL", "Parque Industrial"
        ALTOS = "ALTOS", "Altos de Santana"
        DOM_PEDRO = "DOM_PEDRO", "Dom Pedro I"
        VISTA_VERDE = "VISTA_VERDE", "Vista Verde"
        JD_AUGUSTO = "JD_AUGUSTO", "Jardim São José"
        OUTROS = "OUTROS", "Outros"

    CATEGORIAS = [
        ('comercio', 'Comércio'),
        ('relacionamento', 'Relacionamento'),
        ('obra', 'Obra'),
        ('bizarro', 'Bizarro'),
        ('outro', 'Outro'),
    ]

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    bairro = models.CharField(choices=Bairro.choices, max_length=50)
    categoria = models.CharField(max_length=20, choices=CATEGORIAS)
    votos_confirmo = models.PositiveIntegerField(default=0)
    votos_mentira = models.PositiveIntegerField(default=0)
    criado_em = models.DateTimeField(auto_now_add=True)

    autor = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self):
        return self.titulo
