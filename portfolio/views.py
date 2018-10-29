from django.shortcuts import render
from .models import Topic

def index(request):
    """pagina inicial de portfolio"""
    return render(request, 'portfolio/index.html')

def topics(request):
    topics = Topic.objects.order_by('date_added')
    context = {'topics' : topics}
    return render(request, 'templates/portfolio/topics.html', context)

# Create your views here.
