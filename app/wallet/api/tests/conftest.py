import random
from decimal import Decimal
from uuid import uuid4

import pytest

from wallet.models import Wallet


@pytest.fixture
def wallet() -> Wallet:
    return Wallet.objects.create(
        label=f"{uuid4()}",
        balance=Decimal(
            f"{random.random() * 1_000_000 * (-1 ** random.choice([1, 2])):.2f}"
        ),
    )
