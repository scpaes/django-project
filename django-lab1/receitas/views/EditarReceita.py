from receitas.models import Receitas
from django.shortcuts import get_object_or_404, redirect, render

def editar_receita(request, receita_id):
    """Edita receita"""
    if request.method == 'POST':
        pass
    receita = get_object_or_404(Receitas, pk=receita_id)
    context = {
        'receita': receita
    }
    return render(request, 'receitas/editar-receita.html', context=context)