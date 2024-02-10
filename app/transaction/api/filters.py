from django_filters import FilterSet, NumberFilter, filters

from transaction.models import Transaction
from wallet.models import Wallet


class TransactionFilterSet(FilterSet):
    wallet = filters.ModelMultipleChoiceFilter(queryset=Wallet.objects.only("id"))

    min_created_at = NumberFilter(field_name="created_at", lookup_expr="gte")
    max_created_at = NumberFilter(field_name="created_at", lookup_expr="lte")

    min_amount = NumberFilter(field_name="amount", lookup_expr="gte")
    max_amount = NumberFilter(field_name="amount", lookup_expr="lte")

    class Meta:
        model = Transaction
        fields = [
            "wallet",
            "min_created_at",
            "max_created_at",
            "min_amount",
            "max_amount",
        ]
