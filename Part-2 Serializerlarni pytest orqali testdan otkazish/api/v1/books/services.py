from typing import Union

from books.models import Book


class BookService(object):
    """ Бизнес логики для книга """

    @classmethod
    def get_books_list(cls):
        books = Book.objects.filter(is_active=True)
        return books

    @classmethod
    def create_book(cls, data: dict):
        authors = data.pop('author')
        book = Book.objects.create(**data)
        book.author.add(*authors)
        return book

    @classmethod
    def update_book(cls, instance: Book, data: dict):
        if data.get('author'):
            authors = data.pop('author')
            instance.author.clear()
            instance.author.add(*authors)
        for key, value in data.items():
            setattr(instance, key, value)
        instance.save()
        return instance

    @classmethod
    def book_detail(cls, id: int) -> Union[Book, bool]:
        try:
            book = Book.objects.get(is_active=True, id=id)
            return book
        except Book.DoesNotExist:
            return False

    @classmethod
    def book_delete(cls, id: int) -> bool:
        try:
            book = Book.objects.get(is_active=True, id=id)
            book.delete()
            return True
        except:
            return False
