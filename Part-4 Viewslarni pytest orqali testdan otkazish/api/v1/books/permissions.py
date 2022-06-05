from rest_framework.permissions import BasePermission

from books.models import Book


class AuthorPermission(BasePermission):
    def has_permission(self, request, view):
        request_user = view.request.user
        try:
            book = Book.objects.get(id=view.kwargs.get('pk'))
            if request_user not in book.author.all():
                return False
            if not request.user.is_authenticated:
                return False
        except Book.DoesNotExist:
            return False
        return request.user.is_active
