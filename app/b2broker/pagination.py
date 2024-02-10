from rest_framework.pagination import LimitOffsetPagination


# default pagination do not provide default_limit and returns all persisted rows
class DefaultLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 25
    max_limit = 100
