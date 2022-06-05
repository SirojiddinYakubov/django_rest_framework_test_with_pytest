from rest_framework import generics, exceptions, status, permissions
from rest_framework.response import Response

from api.v1.books import serializers
from api.v1.books.services import BookService
from books.models import Book


class BookAPIViewMixin(generics.GenericAPIView):
    queryset = Book.objects.filter(is_active=True)
    serializer_class = serializers.BookSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        obj = BookService.book_detail(id=self.kwargs.get('pk'))
        if not obj:
            raise exceptions.NotFound({"detail": "Объект не найден"})
        return obj

    def get_queryset(self):
        qs = BookService.get_books_list()
        return qs

    def perform_destroy(self, instance):
        response = BookService.book_delete(id=instance.id)
        if not response:
            raise exceptions.ValidationError({"detail": "Произошла ошибка"})
        return Response(status=status.HTTP_204_NO_CONTENT)
