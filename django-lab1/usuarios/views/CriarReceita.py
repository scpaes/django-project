from django.shortcuts import render


def criar_receita(request):
    return render(request, 'usuarios/criar-receita.html', status=200)