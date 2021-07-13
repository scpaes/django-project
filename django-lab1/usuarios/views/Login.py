from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth


def login(request):

    if request.method == 'POST':
        email = request.POST.get('email')
        senha = request.POST.get('senha')

        if email == '' or senha == '':
            print('Os campos de e-mail e senha não podem ser vazios')
            return redirect(to='login')

        if User.objects.filter(email=email).exists():
            username = User.objects.filter(email=email).values_list('username', flat=True).get()
            user_auth = auth.authenticate(request, username=username, password=senha)

            if user_auth is not None:
                auth.login(request, user_auth)
                return redirect(to='dashboard')
            return redirect('login')
        else:
            print('Email ou senha estão incorretos')
            render(request, 'usuarios/login.html', status=401)        
    return render(request, 'usuarios/login.html', status=200)