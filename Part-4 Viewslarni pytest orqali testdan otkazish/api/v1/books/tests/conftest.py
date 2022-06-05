import pytest
from pytest_factoryboy import register
from rest_framework.test import APIClient

from api.v1.books.tests.factories import BookFactory, CategoryFactory, UserFactory

register(UserFactory)
register(CategoryFactory)
register(BookFactory)


@pytest.fixture
def api_client():
    def _api_client(user=None):
        client = APIClient()
        if user:
            client.force_authenticate(user)
        return client

    return _api_client
