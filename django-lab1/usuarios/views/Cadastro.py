from django.shortcuts import redirect
from django.contrib.auth.models import User
from usuarios.views import *

def cadastro(request):

    if request.method == 'POST':
        nome = request.POST.get('nome')
        email = request.POST.get('email')
        senha = request.POST.get('password')
        senha2 = request.POST.get('password2')

        if not nome.strip():
            print('O campo nome não pode ficar em branco.')
            return redirect(to='cadastro')
        if not email.strip():
            print('O campo e-mail não pode ficar em branco')
            return redirect(to='cadastro')
        if senha != senha2:
            print('As senhas não batem')
            return redirect(to='cadastro')

        if User.objects.filter(email=email).exists():
            print('Usuário já cadastrado')
            return redirect(to='cadastro')
        
        user = User.objects.create_user(username=nome, email=email, password=senha)
        user.save()
        print('Usuário cadastrado com sucesso')
        return redirect(to='login')

    return render(request, 'usuarios/cadastro.html', status=200)