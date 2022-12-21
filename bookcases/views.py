from django.shortcuts import render
from django.views import generic
from .models import Book, Bookcase, Bookcase_book


class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.filter(approved=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6
