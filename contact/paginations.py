from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class ContactPagination(PageNumberPagination):
    """Pagination for contacts"""
    page_size = 10

    def get_paginated_response(self, data):
        return Response({
            'count': self.page.paginator.count,
            'page': self.page.number,
            'page_next': self.page.number + 1 if self.get_next_link() else None,
            'page_previous': self.page.number - 1 if self.get_previous_link() else None,
            'next': self.get_next_link(),
            'previous': self.get_previous_link(),
            'results': data
        })
