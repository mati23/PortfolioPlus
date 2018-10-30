from django.shortcuts import render
from .models import Topic

def index(request):
    """pagina inicial de portfolio"""
    return render(request, 'portfolio/index.html')

def topics(request):
    """pagina inicial de portfolio"""
    return render(request, 'portfolio/topics.html')

# Create your views here.
