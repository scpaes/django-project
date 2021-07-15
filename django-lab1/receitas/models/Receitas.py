from django.db.models.deletion import CASCADE
from receitas.models import *
from datetime import datetime
from django.contrib.auth.models import User

class Receitas(models.Model):
    nome_receita = models.CharField(max_length=200)
    ingredientes = models.TextField()
    modo_preparo = models.TextField()
    tempo_preparo = models.IntegerField()
    rendimento = models.CharField(max_length=100)
    categoria = models.CharField(max_length=100)
    date_receita = models.DateTimeField(default=datetime.now, blank=True)
    publicada = models.BooleanField(default=False)
    pessoa = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)

    foto_receita = models.ImageField(upload_to='fotos/%d/%m/%Y/', blank=True)