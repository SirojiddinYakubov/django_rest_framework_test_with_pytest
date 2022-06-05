import pytest
from django.contrib.auth.models import User
from django.urls import reverse_lazy
from rest_framework import status


@pytest.fixture
def book_list_data(request, user_factory, api_client):
    request_user = user_factory.create()
    data = {
        'success-with-registered-user':
            (status.HTTP_200_OK, api_client(user=request_user)),
        'error-with-unregistered-user':
            (status.HTTP_401_UNAUTHORIZED, api_client(user=None))
    }
    return data[request.param]


@pytest.mark.django_db
@pytest.mark.parametrize('book_list_data', ['success-with-registered-user', 'error-with-unregistered-user'],
                         indirect=True)
def test_list_book(book_list_data, book_factory):
    book_factory.create_batch(5)
    url = reverse_lazy('books:book_list')
    status_code, client = book_list_data
    # send get request
    response = client.get(url)
    # check response
    assert response.status_code == status_code
    if response.status_code == status.HTTP_200_OK:
        assert response.json()


@pytest.fixture
def book_create_data(request, category_factory, user_factory, api_client):
    category = category_factory.create(title="Fantastika")
    author = user_factory.create()
    request_user = user_factory.create()
    data = {
        'success-with-registered-user': (
            status.HTTP_201_CREATED, api_client(user=request_user), {
                "title": "Garri Poter", "desc": "This is description", "pub_date": "2022-01-01",
                "category": category.id, "author": [author.id]
            }
        ),
        'error-with-unregistered-user': (
            status.HTTP_401_UNAUTHORIZED, api_client(user=None), {
                "title": "Garri Poter", "desc": "This is description", "pub_date": "2022-01-01",
                "category": category.id, "author": [author.id]
            }
        ),
    }
    return data[request.param]


@pytest.mark.django_db
@pytest.mark.parametrize("book_create_data", ['success-with-registered-user', 'error-with-unregistered-user'],
                         indirect=True)
def test_book_create(book_create_data):
    url = reverse_lazy('books:book_create')
    status_code, client, data = book_create_data
    # send post request
    response = client.post(url, data=data)
    # check response
    assert response.status_code == status_code
    if response.status_code == status.HTTP_201_CREATED:
        assert response.json()


@pytest.fixture
def book_update_data(request, category_factory, user_factory, api_client, book_factory):
    category = category_factory.create(title="Fantastika")
    author = user_factory.create(first_name="Djoan", last_name="Rouling")
    book = book_factory.create(title="Garri Poter")
    book.author.add(author)
    data = {
        'success-with-registered-user': (
            status.HTTP_200_OK, book, api_client(user=author), {
                "title": "Garri Poter", "desc": "This is description", "pub_date": "2022-01-01",
                "category": category.id, "author": [author.id]
            }
        ),
        'error-with-unregistered-user': (
            status.HTTP_401_UNAUTHORIZED, book, api_client(user=None), {
                "title": "Garri Poter", "desc": "This is description", "pub_date": "2022-01-01",
                "category": category.id, "author": [author.id]
            }
        ),
        'error-book-author': (
            status.HTTP_403_FORBIDDEN, book_factory.create(), api_client(user=author), {
                "title": "Garri Poter", "desc": "This is description", "pub_date": "2022-01-01",
                "category": category.id, "author": [author.id]
            }
        ),
    }
    return data[request.param]


@pytest.mark.django_db
@pytest.mark.parametrize("book_update_data",
                         ["success-with-registered-user", "error-with-unregistered-user", "error-book-author"],
                         indirect=True)
def test_book_update(book_update_data):
    status_code, instance, client, data = book_update_data
    url = reverse_lazy('books:book_update', kwargs={'pk': instance.id})
    # send patch request
    response_patch = client.patch(url, data=data)
    # send put request
    response_put = client.put(url, data=data)
    # check response
    assert response_patch.status_code == status_code
    assert response_put.status_code == status_code
    if response_patch.status_code == status.HTTP_200_OK:
        assert response_patch.json()
    if response_put.status_code == status.HTTP_200_OK:
        assert response_put.json()


@pytest.fixture
def book_detail_data(request, book_factory, user_factory, api_client):
    book = book_factory.create()
    data = {
        'success-with-registered-user': (
            status.HTTP_200_OK, api_client(user=user_factory.create()), book.id
        ),
        'error-with-unregistered-user': (
            status.HTTP_401_UNAUTHORIZED, api_client(user=None), book.id
        ),
        'error-with-invalid-id': (
            status.HTTP_404_NOT_FOUND, api_client(user=user_factory.create()), 123
        ),
    }
    return data[request.param]


@pytest.mark.django_db
@pytest.mark.parametrize("book_detail_data",
                         ["success-with-registered-user", "error-with-unregistered-user", "error-with-invalid-id"],
                         indirect=True)
def test_detail_book(book_detail_data):
    status_code, client, instance_id = book_detail_data
    url = reverse_lazy('books:book_detail', kwargs={'pk': instance_id})
    # send get request
    response = client.get(url)
    # check response
    assert response.status_code == status_code
    if response.status_code == status.HTTP_200_OK:
        assert response.json()


@pytest.fixture
def book_delete_data(request, book_factory, user_factory, api_client):
    book = book_factory.create()
    data = {
        'success-with-registered-user': (
            status.HTTP_204_NO_CONTENT, api_client(user=user_factory.create()), book.id
        ),
        'error-with-unregistered-user': (
            status.HTTP_401_UNAUTHORIZED, api_client(user=None), book.id
        ),
        'error-with-invalid-id': (
            status.HTTP_404_NOT_FOUND, api_client(user=user_factory.create()), 123
        ),
    }
    return data[request.param]


@pytest.mark.django_db
@pytest.mark.parametrize("book_delete_data",
                         ["success-with-registered-user", "error-with-unregistered-user", "error-with-invalid-id"],
                         indirect=["book_delete_data"])
def test_delete_book(book_delete_data):
    status_code, client, instance_id = book_delete_data
    # send delete request
    url = reverse_lazy('books:book_delete', kwargs={'pk': instance_id})
    response = client.delete(url)
    # check response
    assert response.status_code == status_code
