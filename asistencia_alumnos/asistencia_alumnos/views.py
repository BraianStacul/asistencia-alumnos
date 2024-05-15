from django.shortcuts import render

from apps.usuarios.models import Usuario

def login(request):
    return render(request, 'login.html', {})

def home(request):
    template_name = 'home.html'

    ctx = {

    }

    return render(request, template_name, ctx)