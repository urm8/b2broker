import pytest
from django.shortcuts import reverse
from pytest import mark
from rest_framework import status
from rest_framework.utils import json

from transaction.factories import TransactionFactory
from transaction.models import Transaction
from wallet.factories import WalletFactory


@mark.django_db
class TestTransactionViewSet:
    @pytest.fixture
    def wallet(self):
        return WalletFactory()

    @pytest.fixture
    def transaction(self, wallet):
        return TransactionFactory(wallet=wallet)

    def test_create_transaction(self, wallet, api_client):
        data = {
            "amount": '10.00',
            "wallet_id": wallet.pk,
            'txid': 'test'
        }

        response = api_client.post(
            reverse("transaction:transaction-list"),
            data=json.dumps(data),
            content_type="application/json",
        )
        assert response.status_code == status.HTTP_201_CREATED, response.json()

        json_ = response.json()
        assert json_["amount"] == data['amount']
        assert json_["wallet"]['id'] == wallet.pk

    def test_list_transactions(self, transaction, api_client):
        response = api_client.get(reverse("transaction:transaction-list"))
        assert response.status_code == status.HTTP_200_OK
        json_ = response.json()
        assert json_["count"] == 1
        assert json_["results"][0]["id"] == transaction.pk

    def test_retrieve_transaction(self, transaction, api_client):
        response = api_client.get(
            reverse("transaction:transaction-detail", kwargs={"pk": transaction.pk})
        )
        assert response.status_code == status.HTTP_200_OK
        json_ = response.json()
        assert json_["id"] == transaction.pk

    def test_delete_transaction(self, transaction, api_client):
        response = api_client.delete(
            reverse("transaction:transaction-detail", kwargs={"pk": transaction.pk})
        )
        assert response.status_code == status.HTTP_204_NO_CONTENT

        with pytest.raises(Transaction.DoesNotExist):
            Transaction.objects.get(id=transaction.id)
