from django.db import models

from apps.clases.models import Clase
from apps.usuarios.models import Usuario

# Create your models here.

class Asistencia(models.Model):
    usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE, related_name="mis_asistencias")
    clase = models.ForeignKey(Clase, on_delete=models.CASCADE, related_name="asistencias")