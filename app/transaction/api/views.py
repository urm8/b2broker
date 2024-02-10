from rest_framework.mixins import (
    CreateModelMixin,
    DestroyModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
)
from rest_framework.viewsets import GenericViewSet

from transaction.api.filters import TransactionFilterSet
from transaction.api.serializers import (
    TransactionCreateSerializer,
    TransactionListSerializer,
    TransactionRetrieveSerializer,
)
from transaction.models import Transaction


class TransactionViewSet(
    GenericViewSet,
    CreateModelMixin,
    ListModelMixin,
    RetrieveModelMixin,
    DestroyModelMixin,
):
    queryset = Transaction.objects.select_related("wallet")
    search_fields = ["taxid", "wallet__label"]

    filterset_class = TransactionFilterSet

    def get_serializer_class(self):
        if self.action == "create":
            return TransactionCreateSerializer
        elif self.action == "retrieve":
            return TransactionRetrieveSerializer
        return TransactionListSerializer
