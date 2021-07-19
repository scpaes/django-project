from django.urls import path

from usuarios.views import (
    Cadastro,
    Dashboard,
    Login,
    Logout,
)

urlpatterns = [
    path('cadastro/', Cadastro.cadastro, name='cadastro'),
    path('login/', Login.login, name='login'),
    path('dashboard/', Dashboard.dashboard, name='dashboard'),
    path('logout/', Logout.logout, name='logout'),
]
