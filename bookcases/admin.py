from django.contrib import admin
from .models import Book
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    prepopulated_fields = {'slug': ('title',)}
    list_display = ('title', 'author', 'approved', 'created_on')
    search_fields = ['title', 'author']
    list_filter = ('approved', 'created_on')
    actions = ['approve_books']

    def approve_books(self, request, queryset):
        queryset.update(approved=True)