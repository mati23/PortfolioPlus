from django.conf.urls import url
from django.urls import path
from django.contrib.auth import views as auth_views

from . import views

app_name = 'users'
urlpatterns = [
    #pagina do login
    path('login/', auth_views.LoginView.as_view(template_name = 'users/login.html')
    ,name='login'),
]
