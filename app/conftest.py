import pytest
from rest_framework.test import APIClient, APIRequestFactory


@pytest.fixture(autouse=True)
def enable_db_access_for_all_tests(db):
    pass


@pytest.fixture(scope="session")
def request_factory() -> APIRequestFactory:
    return APIRequestFactory()


@pytest.fixture(scope='session')
def api_client() -> APIClient:
    return APIClient()
