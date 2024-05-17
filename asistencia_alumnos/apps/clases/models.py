from django.db import models

# Create your models here.

class Clase(models.Model):
    fecha = models.DateField()

'''
class NuevaTabla(models.Model):
    pass 

    class Meta:
        db_table = 'nueva_tabla'
'''
