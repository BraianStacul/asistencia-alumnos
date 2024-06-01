from django.shortcuts import render, redirect

class VerificarPermisosMixins:
    def dispatch(self, request, *args, **kwargs):

        if not self.request.user.es_profesor and not self.request.user.es_profesor:
            return redirect("error_permisos")

        return super(VerificarPermisosMixins, self).dispatch(request, *args, **kwargs)