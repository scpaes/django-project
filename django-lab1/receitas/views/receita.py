from receitas.views import *
from django.shortcuts import get_list_or_404, get_object_or_404

def receita(request, id):
    receita = get_object_or_404(Receitas, pk = id)

    context = {
        'receita': receita
    }
    return render(request, 'receitas/receita.html', context=context, status=200)