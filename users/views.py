from django.shortcuts import render
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.contrib.auth import logout


# Create your views here.

def logout_view(request):
    """Faz o logout do usuario"""
    logout(request)
    return HttpResponseRedirect(reverse('portfolio:index'))
