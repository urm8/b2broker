from transaction.models import Transaction
from wallet.models import Wallet


class TestTransactionModel:
    def test_save_method_updates_balance_of_related_wallet(self, wallet):
        wallet = Wallet.objects.create(wallet=wallet)
        transaction = Transaction(wallet=wallet, amount=10)
        assert not wallet.balance
        transaction.save()
        assert wallet.balance == 10

    def test_delete_method_subtracts_amount_from_related_wallets_balance(self):
        wallet = Wallet.objects.create()
        transaction = Transaction(wallet=wallet, amount=10)
        assert not wallet.balance
        transaction.save()
        assert wallet.balance == 10
        transaction.delete()
        assert wallet.balance == 0
