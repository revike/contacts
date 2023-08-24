from django_filters import FilterSet, CharFilter
from django.db.models import Q


class ContactFilter(FilterSet):
    """Filter for contacts"""
    search = CharFilter(method='search_filter')

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
