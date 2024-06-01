from django.shortcuts import render, redirect

# Create your views here.
from apps.clases.models import Clase
from apps.usuarios.models import Usuario
from apps.utils.decorators import verificar_permisos

from .models import Asistencia

@verificar_permisos()
def marcar_asistencia(request, clase_id):
    template_name = 'asistencias/marcar_asistencia.html'
    
    todos_los_presentes = []
    for a in Asistencia.objects.filter(clase__id=clase_id):
        todos_los_presentes.append(a.usuario.id)

    ctx = {
        "usuarios" : Usuario.objects.all(),
        "clase" : Clase.objects.get(id=clase_id),
        "presentes" : todos_los_presentes
    }

    return render(request, template_name, ctx)

@verificar_permisos()
def crear_asistencia(request, clase_id, usuario_id):
    a = Asistencia.objects.create(
        usuario_id = usuario_id,
        clase_id = clase_id
    )

    return redirect("asistencias:marcar_asistencia", clase_id = clase_id)