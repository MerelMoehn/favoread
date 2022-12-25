from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book, Bookcase_book
from django.contrib.auth.models import User
from .forms import SubmitForm
from django.core.exceptions import ObjectDoesNotExist


class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.filter(approved=True).order_by('-created_on')[:3]
    template_name = 'index.html'
    paginate_by = 6


class SubmitBook(View):

    def get(self, request, *args, **kwargs):
        return render(
            request,
            'submit_book.html',
            {
                "submit_book": SubmitForm()
            }
        )

    def post(self, request, *args, **kwargs):

        submit_form = SubmitForm(request.POST, request.FILES)
        # to add the book to the Book model
        if submit_form.is_valid():
            new_book = submit_form.save()

        # to add the book as an instance to the Bookcase_book model
            new_bookcase_book = Bookcase_book.objects.create(book_id=new_book, bookcase_owner=request.user)

        else:
            submit_form = SubmitForm()

        return render(
            request,
            "submit_book.html",
        )


class BookDetail(View):
    def get(self, request, slug, *args, **kwargs):
        queryset = Book.objects.filter(approved=True)
        book = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "book_detail.html",
            {
                "book": book,
            },
        )


class BookcaseOwners(generic.ListView):
    model = Bookcase_book
    queryset = Bookcase_book.objects.all()
    template_name = 'get_inspired.html'

class BookcaseBookList(View):
    def get(self, request, *args, **kwargs):
        queryset = Bookcase.objects.all()
        bookcase_books = get_object_or_404(queryset, bookcase_owner=request.user)

        return render(
            request,
            "bookcase_detail.html",
            {
                "books": bookcase_books,
            },
        )
