"""Padroes de URLS de portfolio"""

from django.conf.urls import url
from . import views

app_name = 'portfolio'
urlpatterns = [
    #pagina inicial
    url('', views.index, name = 'index'),
    url('topics/$', views.topics, name = 'topics')

]
