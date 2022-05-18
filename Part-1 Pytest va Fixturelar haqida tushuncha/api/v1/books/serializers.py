from django.contrib.auth import get_user_model
from rest_framework import serializers

from api.v1.books.services import BookService
from api.v1.common.serializers import CategorySerializer, UserSerializer
from books.models import Book

User = get_user_model()


class BookSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = [
            'id',
            'title',
            'category',
            'desc',
            'author',
            'pub_date',
        ]

    def create(self, validated_data):
        book = BookService.create_book(validated_data)
        return book

    def update(self, instance, validated_data):
        book = BookService.update_book(instance, validated_data)
        return book

    def to_representation(self, instance):
        context = super().to_representation(instance)
        context['category'] = CategorySerializer(instance.category).data
        context['author'] = UserSerializer(instance.author, many=True).data
        return context
