import django_filters

from .models import Usuario

class UsuarioFilter(django_filters.FilterSet):

    first_name = django_filters.CharFilter(lookup_expr='icontains')

    class Meta:
        model = Usuario
        fields =  ["username", "first_name", "last_name"]   