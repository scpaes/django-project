from django.shortcuts import redirect, render


def dashboard(request):
    if request.user.is_authenticated:
        return render(request, 'usuarios/dashboard.html')
    return redirect(to='index')
