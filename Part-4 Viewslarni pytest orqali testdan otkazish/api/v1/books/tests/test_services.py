import datetime
import pytest
from api.v1.books import services
from books.models import Book


@pytest.fixture
def book_create_update_data(request, category_factory, user_factory, book_factory):
    author1, author2 = user_factory.create_batch(2)
    category1, category2 = category_factory.create_batch(2)
    instance = book_factory.create()
    data = {
        'valid-data': (
            True, instance, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": datetime.date(2022, 1, 1), "category": category1,
                "author": [author1]
            }, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": datetime.date(2022, 1, 1), "category": category1,
                "author": [author1]
            },

        ),
        'invalid-title': (
            False, instance, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": datetime.date(2022, 1, 1), "category": category1,
                "author": [author1]
            },
            {
                "title": "Muz qo'shig'i", "desc": "This is description",
                "pub_date": datetime.date(2022, 1, 1), "category": category1,
                "author": [author1]
            }
        ),
        'invalid-pub-date': (
            False, instance, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": datetime.date(2022, 1, 1), "category": category1,
                "author": [author1]
            },
            {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": datetime.date(2022, 1, 10), "category": category1,
                "author": [author1]
            }
        ),
        'invalid-category': (
            False, instance, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": datetime.date(2022, 1, 1), "category": category1,
                "author": [author1]
            },
            {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": datetime.date(2022, 1, 1), "category": category2,
                "author": [author1]
            }
        ),
        'invalid-author': (
            False, instance, {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": datetime.date(2022, 1, 1), "category": category1,
                "author": [author1]
            },
            {
                "title": "Garri Poter", "desc": "This is description",
                "pub_date": datetime.date(2022, 1, 1), "category": category1,
                "author": [author2]
            }
        ),

    }
    return data[request.param]


@pytest.mark.django_db
@pytest.mark.parametrize("book_create_update_data",
                         ['valid-data', 'invalid-title', 'invalid-pub-date', 'invalid-category',
                          'invalid-author'], indirect=True)
def test_book_create(book_create_update_data):
    validity, _, data, confirm_data = book_create_update_data
    book = services.BookService.create_book(data=data)
    result = all([
        book.title == confirm_data.get('title'),
        book.desc == confirm_data.get('desc'),
        book.pub_date == confirm_data.get('pub_date'),
        book.category == confirm_data.get('category'),
        list(book.author.all()) == confirm_data.get('author')
    ])
    assert validity == result
    if validity:
        assert Book.objects.get(title=confirm_data.get('title'))
        assert 2 == Book.objects.count()


@pytest.mark.django_db
@pytest.mark.parametrize("book_create_update_data", ['valid-data', 'invalid-title', 'invalid-pub-date', 'invalid-category',
                          'invalid-author'], indirect=True)
def test_update_book(book_create_update_data):
    validity, instance, data, confirm_data = book_create_update_data
    book = services.BookService.update_book(instance=instance, data=data)
    result = all([
        book.title == confirm_data.get('title'),
        book.desc == confirm_data.get('desc'),
        book.pub_date == confirm_data.get('pub_date'),
        book.category == confirm_data.get('category'),
        list(book.author.all()) == confirm_data.get('author')
    ])
    assert validity == result
    if validity:
        assert Book.objects.get(id=book.id)
        assert 1 == Book.objects.count()


@pytest.fixture
def book_detail_delete_data(request, book_factory):
    book = book_factory.create()
    data = {
        'valid-data': (True, book.id),
        'invalid-data': (False, 123),
    }
    return data[request.param]

@pytest.mark.parametrize("book_detail_delete_data", ['valid-data', 'invalid-data'], indirect=True)
@pytest.mark.django_db
def test_book_detail(book_detail_delete_data):
    validity, instance_id = book_detail_delete_data
    book = services.BookService.book_detail(id=instance_id)
    assert validity == bool(book)
    if validity:
        db_book = Book.objects.get(id=instance_id)
        assert bool(db_book)


@pytest.mark.parametrize("book_detail_delete_data", ['valid-data', 'invalid-data'], indirect=True)
@pytest.mark.django_db
def test_book_delete(book_detail_delete_data):
    validity, instance_id = book_detail_delete_data
    book = services.BookService.book_delete(id=instance_id)
    assert validity == book
    if validity:
        db_books = Book.objects.filter(id=instance_id)
        assert not db_books.exists()


@pytest.fixture
def book_list_data(request):
    data = {
        'valid-data': (True, 10, 10),
        'invalid-data': (False, 7, 5)
    }
    return data[request.param]

@pytest.mark.parametrize("book_list_data", ['valid-data', 'invalid-data'], indirect=True)
@pytest.mark.django_db
def test_books_list(book_list_data, book_factory):
    validity, batch_size, count = book_list_data
    book_factory.create_batch(batch_size)
    books = services.BookService.get_books_list()
    db_books = Book.objects.filter(is_active=True)
    assert db_books.count() == books.count()
    assert validity == (books.count() == count)

