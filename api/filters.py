from django_filters import rest_framework as filters

from .models import Terminal


class TerminalFilter(filters.FilterSet):
    serial_number = filters.CharFilter(
        field_name='serial_number', lookup_expr='contains')
    part_number = filters.CharFilter(
        field_name='part_number', lookup_expr='contains')
    acquirer = filters.NumberFilter(field_name='acquirer')
    status = filters.NumberFilter(field_name='status')
    model = filters.NumberFilter(field_name='model')
    location = filters.NumberFilter(field_name='location')
    notes = filters.CharFilter(
        field_name='notes', lookup_expr='contains')

    class Meta:
        model = Terminal
        fields = ['serial_number', 'part_number', 'acquirer',
                  'status', 'model', 'location', 'notes']
