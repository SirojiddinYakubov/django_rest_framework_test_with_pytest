from django.contrib import admin

from books.models import (Book)


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'desc', 'pub_date', 'is_active']
    list_display_links = ['title']
    list_filter = ['is_active', 'pub_date', ]
    save_on_top = True
