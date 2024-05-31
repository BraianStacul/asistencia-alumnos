from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView
from django.views.generic.list import ListView
from django.urls import reverse_lazy

from .forms import ClaseForm
from .models import Clase

# Create your views here.
'''
def listar_clases(request):
    template_name = 'clases/lista.html'

    ctx = {
        "clases" : Clase.objects.all().order_by("-fecha")
    }

    return render(request, template_name, ctx)
'''

class ListarClases(ListView):
    template_name = 'clases/lista.html'
    model = Clase
    context_object_name = 'clases'
    #Paginación
    paginate_by = 20

    def get_context_data(self, **kwargs):
        ctx = super(ListarClases, self).get_context_data(**kwargs)
        ctx["icono"] = "o"
        return ctx
    
    def get_queryset(self):
        return self.model.objects.all().order_by('-fecha')

class CrearClase(CreateView):
    template_name = "clases/crear.html"
    model = Clase
    form_class = ClaseForm
    success_url = reverse_lazy("clases:listar_clases")

class EditarClase(UpdateView):
    template_name = "clases/editar.html"
    model = Clase
    form_class = ClaseForm
    success_url = reverse_lazy("clases:listar_clases")

class MisClases(ListView):
    template_name = 'clases/mis_clases.html'
    model = Clase
    context_object_name = 'clases'
    #Paginación
    paginate_by = 20

    def get_queryset(self):
        return self.model.objects.all().order_by('-fecha')