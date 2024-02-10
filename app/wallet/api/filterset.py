from django_filters import NumberFilter
from django_filters.rest_framework import FilterSet

from wallet.models import Wallet


class WalletFilterSet(FilterSet):
    min_balance = NumberFilter(field_name="balance", lookup_expr="gte")
    max_balance = NumberFilter(field_name="balance", lookup_expr="lte")

    class Meta:
        model = Wallet
        fields = ["min_balance", "max_balance"]
