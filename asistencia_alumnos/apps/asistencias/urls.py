from django.urls import path

from . import views

app_name = "asistencias"

urlpatterns = [
    path('marcar-asistencia/<int:clase_id>/', views.marcar_asistencia, name='marcar_asistencia'),
    path('crear_asistencia/clase/<int:clase_id>/usuario/<int:usuario_id>/', views.crear_asistencia, name='crear_asistencia')
] 