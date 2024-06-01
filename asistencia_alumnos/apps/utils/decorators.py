from django.shortcuts import redirect

def verificar_permisos():

    def deco_verificar_permisos(f):

        def check(request, *args, **kwargs):
            if not request.user.es_profesor and not request.user.es_profesor:
                return redirect("error_permisos")
            
            return f(request, *args, **kwargs)

        return check

    return deco_verificar_permisos