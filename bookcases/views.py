from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from .models import Book, Bookcase_book
from .forms import SubmitForm


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
            new_bookcase_book = Bookcase_book.objects.create(book=new_book, bookcase_owner=request.user)

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


class Bookcases(generic.ListView):
    model = Bookcase_book
    context_object_name = 'bookcases'
    queryset = Bookcase_book.objects.order_by('bookcase_owner').distinct('bookcase_owner')
    template_name = 'bookcases.html'
    paginate_by = 6


class AddBook(View):

    def post(self, request, slug, *args, **kwargs):
        current_user = request.user
        book_to_add = get_object_or_404(Book, slug=slug)
        
        if not Bookcase_book.objects.filter(bookcase_owner=current_user, book=book_to_add).exists():
            new_bookcase_book = Bookcase_book.objects.create(book=book_to_add, bookcase_owner=current_user)
            messages.success(request, 'The book is added to your bookcase', extra_tags='add_book')
            return HttpResponseRedirect(reverse('book_detail', args=[slug]))
        else:
            messages.error(request, 'This book is already in your bookcase', extra_tags='add_book')
            return HttpResponseRedirect(reverse('book_detail', args=[slug]))


class UserBookcase(View):
    def get(self, request, *args, **kwargs):
        current_owner = request.user
        bookcase_books = Bookcase_book.objects.filter(bookcase_owner=current_owner, book__approved=True)

        return render(
            request,
            "user_bookcase.html",
            {
                "books": bookcase_books,
                "user": current_owner,
            },
        )


class DeleteBook(View):

    def post(self, request, book, *args, **kwargs):
        current_user = request.user
        book_to_delete = get_object_or_404(Bookcase_book, book=book, bookcase_owner=current_user)
        book_to_delete.delete()
        return HttpResponseRedirect(reverse('user_bookcase'))


class UpdateStatus(View):

    def post(self, request, book, *args, **kwargs):
        current_user = request.user
        book_to_update = get_object_or_404(Bookcase_book, book=book, bookcase_owner=current_user)
        status_passed = request.GET.get("status")
        book_to_update.status = status_passed
        book_to_update.save()
        return HttpResponseRedirect(reverse('user_bookcase'))


class VisitBookcase(View):
    def get(self, request, owner, *args, **kwargs):
        selected_owner = owner
        bookcase_books = Bookcase_book.objects.filter(bookcase_owner=selected_owner, book__approved=True)
        selected_user = User.objects.filter(id=selected_owner)

        return render(
            request,
            "bookcase_detail.html",
            {
                "books": bookcase_books,
                "user": selected_user,
            },
        )