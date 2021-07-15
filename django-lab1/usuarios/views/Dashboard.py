from django.shortcuts import redirect, render
from receitas.models.Receitas import Receitas


def dashboard(request):
    if request.user.is_authenticated:

        receitas = Receitas.objects.order_by(
            '-date_receita').filter(pessoa=request.user.id)

        context = {
            'receitas': receitas
        }
        return render(request, 'usuarios/dashboard.html', context)
    return redirect(to='index')
