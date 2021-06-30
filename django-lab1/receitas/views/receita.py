from receitas.views import *

def receita(request):
    return render(request, 'receitas/receita.html', status=200)