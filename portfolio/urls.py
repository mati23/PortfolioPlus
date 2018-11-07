"""Padroes de URLS de portfolio"""

from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'portfolio'
urlpatterns = [
    #pagina inicial
    path('', views.index, name = 'index'),
    path('topics/', views.topics, name = 'topics'),
    path('new_topic/', views.new_topic, name = 'new_topic'),

]
