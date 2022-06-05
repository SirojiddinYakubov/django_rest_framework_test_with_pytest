from rest_framework import generics

from api.v1.books import mixins
from api.v1.books.permissions import AuthorPermission


class BookListAPIView(mixins.BookAPIViewMixin, generics.ListAPIView):
    """ Список книги """
    pass


class BookCreateAPIView(mixins.BookAPIViewMixin, generics.CreateAPIView):
    """ Создать книгу """
    pass


class BookUpdateAPIView(mixins.BookAPIViewMixin, generics.UpdateAPIView):
    """ Редактировать книгу """
    permission_classes = [AuthorPermission]


class BookDetailAPIView(mixins.BookAPIViewMixin, generics.RetrieveAPIView):
    """ О книге подробно """
    pass


class BookDeleteAPIView(mixins.BookAPIViewMixin, generics.DestroyAPIView):
    """ Удалить книгу """
    pass
