import pytest
from rest_framework.test import APIRequestFactory


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope="session")
def request_factory() -> APIRequestFactory:
    return APIRequestFactory()
