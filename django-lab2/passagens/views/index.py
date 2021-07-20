from django.shortcuts import render
from passagens.forms import forms

def index(request):
    """Index view"""
    form = forms.PassagemForm()
    context = {
        'form': form
    }
    return render(request, 'index.html', context)