from rest_framework import pagination


class UsersPagination(pagination.PageNumberPagination):
    """
    Paginator for views
    Example request: http://localhost:8000/api/users?p=2&page_size=5
    """
    page_size = 10
    page_size_query_param = 'page_size'
    max_page_size = 10
    page_query_param = 'p'