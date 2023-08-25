from django.utils.translation import gettext_lazy
from django.core.exceptions import FieldError
from django.db.models import Q
from django_filters import FilterSet, CharFilter
from rest_framework.exceptions import ValidationError


class ContactFilter(FilterSet):
    """Filter for contacts"""
    search = CharFilter(method='search_filter')
    sort = CharFilter(method='sort_filter')

    @classmethod
    def search_filter(cls, queryset, _, value):
        if value:
            filter_list = Q()
            value_list = value.split()
            for obj in value_list:
                filter_list = filter_list | Q(first_name__icontains=obj) | Q(last_name__icontains=obj)
            return queryset.filter(
                Q(first_name__icontains=value) | Q(last_name__icontains=value) | filter_list).distinct()
        return queryset

    @classmethod
    def sort_filter(cls, queryset, _, value):
        if value:
            try:
                return queryset.order_by(value)
            except FieldError as error:
                message = gettext_lazy('In reverse order with -.Example, sort=-created.')
                raise ValidationError({'detail': f'{error} {message}'})
        return queryset
