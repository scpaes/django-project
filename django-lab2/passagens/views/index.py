from django.shortcuts import render

def index(request):
    """Index view"""
    return render(request, 'index.html')