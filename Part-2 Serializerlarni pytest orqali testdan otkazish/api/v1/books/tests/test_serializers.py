import pytest

from api.v1.books import serializers


@pytest.fixture
def book_create_update_data_for_check_serializer(request, category_factory, user_factory):
    author1 = user_factory.create()
    author2 = user_factory.create()
    category = category_factory.create(title="Fantastika")
    data = {
        'complete-data': (
            True, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": "2022-05-11", "category": category.id, "author": [author1.id, author2.id]
            }
        ),
        'missing-title': (
            False, {
                "desc": "This is description", "pub_date": "2022-05-11", "category": category.id,
                "author": [author1.id, author2.id]
            }
        ),
        'empty-title': (
            False, {
                "title": "", "desc": "This is description", "pub_date": "2022-05-11", "category": category.id,
                "author": [author1.id, author2.id]
            }
        ),
        'invalid-date-format': (
            False, {
                "title": "Garri Poter", "desc": "This is description", "pub_date": "11-05-2022",
                "category": category.id,
                "author": [author1.id, author2.id]
            }
        ),
        'missing-desc': (
            False, {
                "title": "Garri Poter", "pub_date": "2021-01-01",
                "category": category.id, "author": [author1.id]
            }
        ),
        'empty-desc': (
            False, {
                "title": "Garri Poter", "desc": "",
                "pub_date": "2022-01-01", "category": category.id, "author": [author1.id]
            }
        ),
        'missing-pub-date': (
            False, {
                "title": "Garri Poter", "desc": "This is description",
                "category": category.id, "author": [author1.id, author2.id]
            }
        ),
        'empty-pub-date': (
            False, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": "", "category": category.id, "author": [author2.id]
            }
        ),
        'missing-category': (
            False, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": "2022-01-01", "author": [author1.id]
            }
        ),
        'invalid-category': (
            False, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": "2022-01-01", "category": 123, "author": [author2.id, author1.id]
            }
        ),
        'empty-category': (
            False, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": "2022-01-01", "category": "", "author": [author1.id]
            }
        ),
        'missing-author': (
            False, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": "2022-01-01", "category": category.id
            }
        ),
        'invalid-author': (
            False, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": "2022-01-01", "category": category.id, "author": [123, 456]
            }
        ),
        'invalid-author-type': (
            False, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": "2022-01-01", "category": category.id, "author": author1.id
            }
        ),
        'empty-author': (
            False, {
                "title": "Garri Poter", "desc": "this is description",
                "pub_date": "2022-01-01", "category": category.id, "author": ['']
            }
        )
    }
    return data[request.param]


@pytest.mark.django_db
@pytest.mark.parametrize("book_create_update_data_for_check_serializer",
                         ['complete-data', 'missing-title', 'empty-title', 'invalid-date-format', 'missing-desc',
                          'empty-desc', 'missing-pub-date', 'empty-pub-date', 'missing-category', 'invalid-category',
                          'empty-category', 'missing-author', 'invalid-author', 'invalid-author-type', 'empty-author'],
                         indirect=True)
def test_book_serializer(book_create_update_data_for_check_serializer: tuple):
    validity, data = book_create_update_data_for_check_serializer
    serializer = serializers.BookSerializer(data=data)
    assert serializer.is_valid() == validity
    if serializer.is_valid():
        serializer.save()
        expected = ['id', 'title', 'category', 'desc', 'author', 'pub_date']
        returned = dict(serializer.data).keys()
        assert sorted(expected) == sorted(returned)
