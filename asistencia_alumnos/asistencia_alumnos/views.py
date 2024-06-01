from django.shortcuts import render, redirect

from django.contrib.auth import authenticate, login as login_django

from apps.usuarios.models import Usuario
from apps.usuarios.forms import FormularioRegistro, FormularioRegistroUsuario

def login(request):

    nombre_usuario = ""
    mensaje_error = None

    if request.method == "POST":
        nombre_usuario = request.POST.get("username") # request.GET.get("username")
        contrasenia = request.POST.get("password") # request.GET.get("password")

        u = authenticate(request, username=nombre_usuario, password=contrasenia)

        if u:
            login_django(request, u)

            return redirect("pagina_principal")
        else:
            mensaje_error = "Usuario y/o contraseña incorrecta"
    
    ctx = {
        "nombre_usuario" : nombre_usuario,
        "mensaje_error" : mensaje_error,
    }

    return render(request, 'login.html', ctx)

def home(request):
    template_name = 'home.html'

    ctx = {

    }

    return render(request, template_name, ctx)

def pagina_error_permisos(request):
    template_name = 'paginas/error_permisos.html'

    ctx = {

    }

    return render(request, template_name, ctx)

def registrarme(request):
    
    template_name = 'registrarme.html'

    form = FormularioRegistroUsuario()

    usuario_todo_bien = None
    
    if request.method == "POST":
        form = FormularioRegistroUsuario(request.POST)
        # Guarduar el usuario
        # username = request.POST.get('username')
        # last_name = request.POST.get('last_name')
        # first_name = request.POST.get('first_name')
        # password = request.POST.get('password')   
        
        if form.is_valid():
            form.save()
            usuario_todo_bien = "Usuario creado correctamente, puede iniciar sesion."
        else:
            print("ERRORES: ", form.errors)

        print("is_valid()----->",form.is_valid())

        '''
        u = Usuario(
            username=username,
            last_name=last_name,
            first_name=first_name,
            password=password
        )

        u.save()
        '''
    
    ctx = {
        'form' : form,
        "usuario_todo_bien" : usuario_todo_bien
    }
    
    return render(request, template_name, ctx)