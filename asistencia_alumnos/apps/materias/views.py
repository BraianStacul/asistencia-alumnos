from django.shortcuts import render

# Create your views here.

from .models import Materia

from django.views.generic.list import ListView

class Listar(ListView):
    template_name = 'materias/listar.html'
    model = Materia
    context_object_name = 'materias'
    #Paginación
    paginate_by = 2
    
    def get_queryset(self):
        return self.model.objects.all().order_by('nombre')
