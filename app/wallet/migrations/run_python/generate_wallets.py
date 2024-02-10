

def code(*args, **kwargs):
    from wallet.factories import WalletFactory
    WalletFactory.create_batch(100, transaction_set__size=500)