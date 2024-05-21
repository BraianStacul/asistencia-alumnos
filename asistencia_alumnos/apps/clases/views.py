from django.shortcuts import render

from .models import Clase

# Create your views here.

def listar_clases(request):
    template_name = 'clases/lista.html'

    ctx = {
        "clases" : Clase.objects.all().order_by("-fecha")
    }

    return render(request, template_name, ctx)