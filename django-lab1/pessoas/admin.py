from django.contrib import admin
from pessoas.models.Pessoa import Pessoa


class PessoaAdmin(admin.ModelAdmin):
    list_display = [
        'nome',
        'email'
    ]
    list_display_links = [
        'nome',
        'email'
    ]

    list_filter = ('nome',)
    search_fields = ('nome',)

admin.site.register(Pessoa, PessoaAdmin)

