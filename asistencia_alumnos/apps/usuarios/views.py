from django.shortcuts import render

# Create your views here.
from django.views.generic.list import ListView
from apps.usuarios.models import Usuario

def listar_usuarios(request):
    template_name = 'usuarios/listar_todos.html'
    lista_usuarios = Usuario.objects.all() # filter(is_superuser = True)

    # print("---->", lista_usuarios)
    # print("iterando usuarios")
    # print("QUERY: ",lista_usuarios.query)
    # for us in lista_usuarios:
    #     print("USUARIOS: ", us)

    ctx = {
        'usuarios' : lista_usuarios,
        # 'fecha_hora' : '29/04/2024 15:28 hs'
    }

    return render(request, template_name, ctx)

class ListarUsuarios(ListView):
    template_name = 'usuarios/listar_todos.html'
    model = Usuario
    context_object_name = 'usuarios'
