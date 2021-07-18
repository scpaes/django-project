from receitas.models import Receitas
from django.shortcuts import get_object_or_404, redirect, render

def editar_receita(request, receita_id):
    if request.method == 'POST':
        pass
    receita = get_object_or_404(Receitas, pk=receita_id)
    context = {
        'receita': receita
    }
    return render(request, 'usuarios/editar-receita.html', context=context)