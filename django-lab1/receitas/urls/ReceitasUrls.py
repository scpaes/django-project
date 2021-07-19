from django.urls import path
from receitas.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', index, name='index'),
    path('<int:id>/', receita, name='receita'),
    path('buscar/', buscar, name='buscar'),
    path('criar/receitas/', criar_receita, name='criar-receita'),
    path('<int:receita_id>/deletar/',
         deletar_receita, name='deletar-receita'),
    path('<int:receita_id>/editar/',
         editar_receita, name='editar-receita'),
    path('atualizar/', atualizar_receita,
         name='atualizar-receita'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
