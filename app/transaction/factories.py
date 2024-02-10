from uuid import uuid4

from factory import LazyFunction, SelfAttribute, SubFactory
from factory.django import DjangoModelFactory
from factory.fuzzy import FuzzyFloat

from transaction.models import Transaction


class TransactionFactory(DjangoModelFactory):
    wallet = SubFactory(
        "wallet.factories.WalletFactory", amount=SelfAttribute("..amount")
    )
    amount = FuzzyFloat(-1_000_000, 1_000_000, precision=18)
    txid = LazyFunction(uuid4)

    class Meta:
        model = Transaction
        django_get_or_create = ["txid"]  # chance is low, but never zero
