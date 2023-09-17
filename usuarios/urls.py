from django.urls import path
from usuarios.views import login, cadastro

urlspatterns = [
    path('login', login, name='login'),
    path('cadastro', cadastro, name='cadastro')
]