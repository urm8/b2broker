from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from rest_framework.validators import UniqueValidator

from transaction.models import Transaction
from wallet.api.serializers import WalletSerializer
from wallet.models import Wallet


class TransactionCreateSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    wallet_id = serializers.PrimaryKeyRelatedField(
        source="wallet", write_only=True, queryset=Wallet.objects.only("id")
    )
    wallet = WalletSerializer(read_only=True)
    txid = serializers.CharField(
        required=True, validators=[UniqueValidator(Transaction.objects.all())]
    )
    amount = serializers.DecimalField(
        max_digits=18, decimal_places=2, coerce_to_string=True
    )

    class Meta:
        model = Transaction
        fields = "__all__"


class TransactionListSerializer(ModelSerializer):
    created_at = serializers.DateTimeField(read_only=True)
    wallet = WalletSerializer(read_only=True)
    txid = serializers.CharField(read_only=True)
    amount = serializers.DecimalField(
        max_digits=18, decimal_places=2, coerce_to_string=True, read_only=True
    )

    class Meta:
        model = Transaction
        fields = "__all__"


class TransactionRetrieveSerializer(TransactionListSerializer):
    pass
