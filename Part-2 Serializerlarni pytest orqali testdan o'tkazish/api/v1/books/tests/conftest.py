from pytest_factoryboy import register
from api.v1.books.tests.factories import BookFactory, CategoryFactory, UserFactory

register(UserFactory)
register(CategoryFactory)
register(BookFactory)
