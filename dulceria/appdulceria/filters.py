import django_filters
from django_filters import DateFilter
from django import forms
from appdulceria.models import Usuario, SolicitudDulces

class UsuarioFiltro(django_filters.FilterSet):
    fecha_n_inicio = DateFilter(field_name="fecha_nacimiento", lookup_expr='gte')
    fecha_n_termino = DateFilter(field_name="fecha_nacimiento", lookup_expr='lte')

    class Meta:
        model = Usuario
        fields = '__all__'
        exclude = ['fecha_nacimiento']

class SolicitudFiltro(django_filters.FilterSet):
    class Meta:
        model = SolicitudDulces
        fields = '__all__'

        widgets = {
            'id_solicitud': forms.NumberInput()
        }