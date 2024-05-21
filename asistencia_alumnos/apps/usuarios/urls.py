from django.urls import path

from . import views

app_name = "usuarios"

urlpatterns = [
    # path('listar-todos/', views.listar_usuarios, name='listar_todos'),
    path('listar-todos/', views.ListarUsuarios.as_view(), name='listar_todos'),
] 