from django.db import models

# Create your models here.

class Categoria(models.Model):
    nombre = models.CharField(max_length=100)

    def __str__(self):
        return self.nombre


class Materia(models.Model):
    nombre = models.CharField(max_length=100)
    categoria = models.ManyToManyField(Categoria)
    # ejemplo = models.OneToOneField
    logo = models.ImageField(null=True, blank=True, upload_to="materias_logo/")
