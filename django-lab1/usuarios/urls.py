from django.urls import path

from usuarios.views import (
    Cadastro,
    Dashboard,
    Login,
    Logout,
    CriarReceita,
    DeletarReceita,
    EditarReceita,
    AtualizarReceita,
)

urlpatterns = [
    path('cadastro/', Cadastro.cadastro, name='cadastro'),
    path('login/', Login.login, name='login'),
    path('dashboard/', Dashboard.dashboard, name='dashboard'),
    path('logout/', Logout.logout, name='logout'),
    path('criar/receitas/', CriarReceita.criar_receita, name='criar-receita'),
    path('<int:receita_id>/deletar/',
         DeletarReceita.deletar_receita, name='deletar-receita'),
    path('<int:receita_id>/editar/', EditarReceita.editar_receita, name='editar-receita'),
    path('atualizar/', AtualizarReceita.atualizar_receita, name='atualizar-receita'),
]
