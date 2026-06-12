from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response


class DefaultPagination(PageNumberPagination):
    """
    a custom pagination for browsable api pages
    """

    page_size = 3

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "all_tasks": self.page.paginator.count,
                "all_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )
