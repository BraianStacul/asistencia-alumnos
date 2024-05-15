from django.contrib import admin
from django.urls import path, include

# from .views import login, home
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='pagina_principal'),
    path('login/', views.login, name='iniciar_sesion'),

    # Includes
    path("usuarios/", include('apps.usuarios.urls')),
    path("clases/", include('apps.clases.urls'))
] 
