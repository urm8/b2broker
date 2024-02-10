from factory import Faker, RelatedFactoryList, post_generation
from factory.django import DjangoModelFactory

from wallet.models import Wallet


class RelatedFactoryVariableList(RelatedFactoryList):
    def call(self, instance, step, context):
        size = context.extra.pop("size", self.size)
        return [
            super(RelatedFactoryList, self).call(instance, step, context)
            for i in range(size)
        ]


class WalletFactory(DjangoModelFactory):
    label = Faker("iban")
    transaction_set = RelatedFactoryVariableList(
        "transaction.factories.TransactionFactory",
        factory_related_name="wallet",
        size=0,
    )

    class Meta:
        model = Wallet
        django_get_or_create = ("label",)

    @post_generation
    def balance(self, create, *_):
        self.balance = sum(t.amount for t in self.transaction_set.only("amount"))
        if create:
            self.save(update_fields=["balance"])
