from receitas.views import *

def index(request):
    return render(request, template_name='receitas/index.html', status=200)