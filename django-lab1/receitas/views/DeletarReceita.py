from django.shortcuts import get_object_or_404, redirect
from receitas.models import Receitas


def deletar_receita(request, receita_id):
    receita = get_object_or_404(Receitas, pk=receita_id)
    receita.delete()
    return redirect('dashboard')