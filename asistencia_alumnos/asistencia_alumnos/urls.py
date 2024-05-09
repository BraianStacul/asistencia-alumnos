from django.contrib import admin
from django.urls import path

# from .views import login, home
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='pagina_principal'),
    path('login/', views.login, name='iniciar_sesion')
] 
