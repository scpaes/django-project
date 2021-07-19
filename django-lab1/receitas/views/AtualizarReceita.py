from django.shortcuts import redirect
from receitas.models.Receitas import Receitas


def atualizar_receita(request):
    if request.method == 'POST':
        receita = Receitas.objects.get(id=request.POST['receita_id'])
        receita.nome_receita = request.POST['nome_receita']
        receita.ingredientes = request.POST['ingredientes']
        receita.modo_preparo = request.POST['modo_preparo']
        receita.tempo_preparo = request.POST['tempo_preparo']
        receita.rendimento = request.POST['rendimento']
        receita.categoria = request.POST['categoria']

        if 'foto_receita' in request.FILES:
            receita.foto_receita = request.FILES['foto_receita']

        receita.save()

        return redirect(to='dashboard')
