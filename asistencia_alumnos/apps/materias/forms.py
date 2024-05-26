from django import forms

from .models import Materia, Categoria

class MateriaForm(forms.ModelForm):

    categoria = forms.ModelMultipleChoiceField(
        queryset=Categoria.objects.all(),
        widget=forms.SelectMultiple()
    )

    class Meta:
        model = Materia
        fields = ["nombre", "categoria"]