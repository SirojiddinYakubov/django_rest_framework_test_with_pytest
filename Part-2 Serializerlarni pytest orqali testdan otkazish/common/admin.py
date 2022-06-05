from django.contrib import admin

from common.models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'is_active']
    list_display_links = ['title']
    list_filter = ['is_active']
    search_fields = ['title']
    save_on_top = True
