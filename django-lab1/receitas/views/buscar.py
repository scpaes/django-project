from receitas.views import *
from receitas.models.Receitas import Receitas

def buscar(request):
    lista_receitas = Receitas.objects.order_by('-date_receita').filter(publicada=True)

    if 'buscar' in request.GET:
        nome_receita = request.GET['buscar']

        if nome_receita:
            lista_receitas = lista_receitas.filter(nome_receita__icontains=nome_receita)

    dados = {
        'receitas': lista_receitas
    }
    return render(request, 'receitas/buscar.html', context=dados, status=200)