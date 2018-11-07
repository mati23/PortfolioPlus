from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse

from .models import Topic
from .forms import TopicForm

def index(request):
    """pagina inicial de portfolio"""
    return render(request, 'portfolio/index.html')

def topics(request):
    """pagina inicial de portfolio"""
    return render(request, 'portfolio/topics.html')

def new_topic(request):
    """Adiciona novo assunto"""
    if request.method != 'POST':
        #nenhum dado submetido; cria formulario em branco
        form = TopicForm()
    else:
        #dados de POST submetidos
        form = TopicForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('portfolio:topics'))

    context = {'form': form}
    return render(request, 'portfolio/new_topic.html', context)

# Create your views here.
