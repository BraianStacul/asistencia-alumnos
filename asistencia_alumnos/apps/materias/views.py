# Create your views here.

from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView
from django.views.generic.list import ListView

from .forms import MateriaForm
from .models import Materia

class Listar(ListView):
    template_name = 'materias/listar.html'
    model = Materia
    context_object_name = 'materias'
    #Paginación
    paginate_by = 20
    
    def get_queryset(self):
        return self.model.objects.all().order_by('nombre')

class Nuevo(LoginRequiredMixin, CreateView):
    template_name = "materias/crear.html"
    model = Materia
    form_class = MateriaForm
    success_url = reverse_lazy("materias:lista")