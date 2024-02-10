from operator import attrgetter
from uuid import uuid4

import pytest
from django.utils import timezone
from rest_framework import status

from wallet.api.views import WalletViewSet
from wallet.models import Wallet


class TestWalletViewSet:
    def test_create(self, request_factory):
        label = str(uuid4())
        request = request_factory.post(
            "/", data={"label": label, "balance": "233232.22"}, format="json"
        )
        create_view = WalletViewSet.as_view({"post": "create"})
        response = create_view(request)
        assert response.status_code == status.HTTP_201_CREATED
        wallets = Wallet.objects.all()
        assert len(wallets) == 1
        (wallet,) = wallets
        assert response.data == {"id": wallet.pk, "label": label, "balance": "0.00"}

    def test_update(self, request_factory, wallet):
        label = str(uuid4())
        request = request_factory.patch(
            "/",
            data={"label": label, "balance": "233232.22"},
            format="json",
        )
        update_view = WalletViewSet.as_view({"patch": "partial_update"})
        response = update_view(request, pk=wallet.pk)
        assert response.status_code == status.HTTP_200_OK
        assert response.data == {
            "id": wallet.pk,
            "label": label,
            "balance": str(wallet.balance),
        }
        wallet.refresh_from_db()
        assert wallet.label == label

    def test_delete(self, request_factory, wallet):
        request = request_factory.delete("/", format="json")
        update_view = WalletViewSet.as_view({"delete": "destroy"})
        response = update_view(request, pk=wallet.pk)
        assert response.status_code == status.HTTP_204_NO_CONTENT
        assert not Wallet.objects.filter(pk=wallet.pk).exists()

    def test_list(self, request_factory, wallet):
        request = request_factory.get("/", format="json")
        list_view = WalletViewSet.as_view({"get": "list"})
        response = list_view(request)
        assert response.status_code == status.HTTP_200_OK

    @pytest.mark.parametrize(
        "lookup,delta,count",
        [
            ("min_balance", 1, 0),
            ("min_balance", 0, 1),
            ("min_balance", -1, 1),
            ("max_balance", 1, 1),
            ("max_balance", 0, 1),
            ("max_balance", -1, 0),
        ],
    )
    def test_list_filter_balance(self, request_factory, wallet, lookup, delta, count):
        request = request_factory.get("/", data={lookup: wallet.balance + delta})
        list_view = WalletViewSet.as_view({"get": "list"})
        response = list_view(request)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == count

    @pytest.mark.parametrize(
        "getter,count",
        [
            (attrgetter("label"), 1),
            (attrgetter("id"), 1),
            (lambda _: timezone.now(), 0),
            (lambda o: o.label[::-1], 0),
        ],
    )
    def test_list_search(self, request_factory, wallet, getter, count):
        request = request_factory.get("/", data={"search": getter(wallet)})
        list_view = WalletViewSet.as_view({"get": "list"})
        response = list_view(request)
        assert response.status_code == status.HTTP_200_OK
        assert len(response.data) == count
