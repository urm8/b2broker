from wallet.api.serializers import WalletSerializer


def test_serializer(wallet):
    serializer = WalletSerializer(instance=wallet)
    data = serializer.data
    assert tuple(data) == ("id", "label", "balance")
    assert data["id"] == wallet.pk
    assert data["label"] == wallet.label
    assert data["balance"] == str(wallet.balance)
