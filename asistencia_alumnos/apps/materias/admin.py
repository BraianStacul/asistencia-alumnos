from django.contrib import admin

from .models import Categoria, Materia

# Register your models here.

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ["id","nombre"]

admin.site.register(Categoria, CategoriaAdmin)


class MateriaAdmin(admin.ModelAdmin):
    list_display = ["id","nombre"]

admin.site.register(Materia, MateriaAdmin)