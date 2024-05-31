from django.db import models

# Create your models here.

class Clase(models.Model):
    fecha = models.DateField()

    def mostrar_fecha(self):
        return self.fecha.strftime('%d-%m-%Y')

    def __str__(self):
        return self.fecha.strftime('%d-%m-%Y')  #str(self.fecha)

    def get_cantidad_presentes(self):
        return self.asistencias.all().count()

'''
class NuevaTabla(models.Model):
    pass 

    class Meta:
        db_table = 'nueva_tabla'
'''
