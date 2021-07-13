from receitas import models
from django.contrib import admin
from receitas.models.Receitas import Receitas

class ReceitaAdmin(admin.ModelAdmin):
    list_display = [
        'id', 'nome_receita',
        'categoria', 'rendimento',
        'publicada'
    ]
    list_display_links = [
        'id', 'nome_receita'
    ]
    search_fields = ('nome_receita',)
    list_filter = ('categoria',)
    list_per_page = 10

admin.site.register(Receitas, ReceitaAdmin)