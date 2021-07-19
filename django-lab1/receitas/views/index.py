from receitas.views import *
from receitas.models.Receitas import Receitas
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage

def index(request):
    receitas = Receitas.objects.filter(publicada=True)
    paginator = Paginator(receitas, 1)
    page = request.GET.get('page')
    receitas_por_pagina = paginator.get_page(page)

    dados = {
        'receitas': receitas_por_pagina
    }
    return render(request,context=dados, template_name='receitas/index.html', status=200)