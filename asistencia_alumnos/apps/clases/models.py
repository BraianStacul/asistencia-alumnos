from django.db import models

# Create your models here.

class Clase(models.Model):
    fecha = models.DateField()

    def get_cantidad_presentes(self):
        return self.asistencias.all().count()

'''
class NuevaTabla(models.Model):
    pass 

    class Meta:
        db_table = 'nueva_tabla'
'''
