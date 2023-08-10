from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response
from rest_framework import status


class CustomPageNumberPagination(PageNumberPagination):

    def get_paginated_response(self, data):
        
        return Response({
            "count": self.page.paginator.count,
            'next': self.get_next_link(),
            "previous": self.get_previous_link(),
            "results": data
        }, status=status.HTTP_200_OK)