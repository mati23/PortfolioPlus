from django.shortcuts import render

def index(request):
    """pagina inicial de portfolio"""
    return render(request, 'portfolio/index.html')

# Create your views here.
