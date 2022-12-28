from django.contrib import admin
from .models import Book, Bookcase_book
from django_summernote.admin import SummernoteModelAdmin


@admin.register(Book)
class BookAdmin(SummernoteModelAdmin):

    list_display = ('title', 'author', 'id', 'approved', 'created_on')
    search_fields = ['title', 'author', 'id']
    list_filter = ('approved', 'created_on')
    actions = ['approve_books']

    def approve_books(self, request, queryset):
        queryset.update(approved=True)


@admin.register(Bookcase_book)
class Bookcase_bookAdmin(SummernoteModelAdmin):
    
    list_display = ('bookcase_owner', 'book')
    search_fields = ['bookcase_owner', 'book']
    list_filter = ('bookcase_owner', 'book')
