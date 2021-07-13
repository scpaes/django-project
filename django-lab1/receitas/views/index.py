from receitas.views import *
from receitas.models.Receitas import Receitas

def index(request):
    receitas = Receitas.objects.filter(publicada=True)

    dados = {
        'receitas': receitas
    }
    return render(request,context=dados, template_name='receitas/index.html', status=200)