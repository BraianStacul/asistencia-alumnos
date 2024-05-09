from django.shortcuts import render

def login(request):
    return render(request, 'login.html', {})

def home(request):
    template_name = 'home.html'
    lista_alumnos = [
        {
            "nombre" : "Lucas",
            "apellido" : "Ibañez",
            "legajo" : 222,
            "habilitado" : True
        },
        {
            "nombre" : "Federico",
            "apellido" : "Aguirre",
            "legajo" : 555,
            "habilitado" : False
        }
    ]

    ctx = {
        'alumnos' : lista_alumnos,
        'fecha_hora' : '29/04/2024 15:28 hs'
    }

    return render(request, template_name, ctx)