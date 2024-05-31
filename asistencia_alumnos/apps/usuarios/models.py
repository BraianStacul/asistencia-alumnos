
from django.contrib.auth.models import AbstractUser
from django.db import models

class Usuario(AbstractUser):
    biografia = models.CharField(max_length=255, null=True, blank=True)

    es_profesor = models.BooleanField(default=False)
    es_alumno = models.BooleanField(default=True)
    es_admin = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.last_name}, {self.first_name} ({self.username})"
    
    def obtener_presentes(self):
        lista_asistencias = []
        print("ASISTENCIAS DE: ", self)
        for asistencia in self.mis_asistencias.all():
            lista_asistencias.append(asistencia.clase.id)

        return lista_asistencias
    
    def obtener_cantidad_presentes(self):
        return len(self.obtener_presentes())