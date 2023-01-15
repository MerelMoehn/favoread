from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from django.contrib import messages
from django.core.paginator import Paginator
from django.db.models import Q
from .models import Book, Bookcase_book
from .forms import SubmitForm


class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.filter(
        approved=True, deleted=False).order_by('-created_on')[:3]
    template_name = 'index.html'


class SubmitBook(View):

    def get(self, request, *args, **kwargs):
        # Render SubmitForm to user to submit a book
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
            new_book = submit_form.save(commit=False)
            new_book.submitted_by = request.user
            new_book = submit_form.save()
            messages.success(request,
                             'Your book has been submitted for review!')

        # to add the book as an instance to the Bookcase_book model
            new_bookcase_book = Bookcase_book.objects.create(
                book=new_book,
                bookcase_owner=request.user
                )

        else:
            submit_form = SubmitForm()
            messages.error(request,
                           'Oeps, something went wrong.'
                           ' Maybe this title already exists.')

        return HttpResponseRedirect(reverse('submit_book'))


class BookDetail(View):
    def get(self, request, slug, *args, **kwargs):
        # Gets a specific book and shows the details
        queryset = Book.objects.filter(approved=True)
        book = get_object_or_404(queryset, slug=slug)

        return render(
            request,
            "book_detail.html",
            {
                "book": book,
            },
        )


class Bookcases(View):
    def get(self, request, *args, **kwargs):
        bookcases = Bookcase_book.objects.order_by(
            'bookcase_owner').distinct('bookcase_owner')
        books = None
        query = None
        if 'q' in request.GET:
            query = request.GET['q']
            if len(query) == 0:
                messages.error(request, "You didn't enter search criteria")
                return HttpResponseRedirect(reverse('bookcases'))

            queries = Q(title__icontains=query) | Q(author__icontains=query)
            books = Book.objects.filter(queries)

            if len(books) == 0:
                messages.error(request, "Your search did not find any matches")
                return HttpResponseRedirect(reverse('bookcases'))

        # To add pagination, show 6 owners per page
        paginator = Paginator(bookcases, 6)
        page_number = request.GET.get('page')
        bookcases = paginator.get_page(page_number)

        context = {
            'books': books,
            'bookcases': bookcases,
            'search_term': query,
            }
        return render(request, 'bookcases.html', context)


class AddBook(View):

    def post(self, request, slug, *args, **kwargs):
        # Adds an existing book to a bookcase of the logged-in user
        # (instance of Bookcase_book)
        current_user = request.user
        book_to_add = get_object_or_404(Book, slug=slug)

        # Checks if the book already exists as
        # instance in Bookcase_book for this user
        if not Bookcase_book.objects.filter(bookcase_owner=current_user,
                                            book=book_to_add).exists():
            new_bookcase_book = Bookcase_book.objects.create(
                book=book_to_add,
                bookcase_owner=current_user)
            messages.success(request, 'The book is added to your bookcase')
            return HttpResponseRedirect(reverse('book_detail', args=[slug]))
        else:
            messages.error(request, 'This book is already in your bookcase')
            return HttpResponseRedirect(reverse('book_detail', args=[slug]))


class UserBookcase(View):
    def get(self, request, *args, **kwargs):
        # Gets all the instances of Bookcase_book for logged-in user
        # to display the bookcase
        current_owner = request.user
        bookcase_books = Bookcase_book.objects.filter(
            bookcase_owner=current_owner, book__approved=True,
            book__deleted=False)

        # To add pagination, show 9 books per page
        paginator = Paginator(bookcase_books, 9)

        page_number = request.GET.get('page')
        bookcase_books = paginator.get_page(page_number)

        return render(
            request,
            "user_bookcase.html",
            {
                "books": bookcase_books,
                "user": current_owner,
            },
        )


class DeleteBookcaseBook(View):

    def post(self, request, book, *args, **kwargs):
        # Deletes a Bookcase_book instance for logged-in user
        current_user = request.user
        book_to_delete = get_object_or_404(
            Bookcase_book, book=book, bookcase_owner=current_user)
        book_to_delete.delete()
        messages.success(request, 'The book is deleted from your bookcase')
        return HttpResponseRedirect(reverse('user_bookcase'))


class DeleteBook(View):

    def post(self, request, book, *args, **kwargs):
        # Sets a Book instance deleted to True (soft delete)
        book_to_delete = get_object_or_404(
            Book, id=book)
        book_to_delete.deleted = True
        book_to_delete.save()
        messages.success(request, 'The book has been deleted.')
        return HttpResponseRedirect(reverse('home'))


class UpdateStatus(View):

    # Allows user to update the reading status of a Bookcase_book
    def post(self, request, book, *args, **kwargs):
        current_user = request.user
        book_to_update = get_object_or_404(
            Bookcase_book, book=book, bookcase_owner=current_user)

        status_passed = request.POST.get('status')

        book_to_update.status = status_passed
        book_to_update.save()
        messages.success(request, 'Reading status has been updated.')
        return HttpResponseRedirect(reverse('user_bookcase'))


class VisitBookcase(View):
    # To display bookcases of other users
    def get(self, request, owner, *args, **kwargs):
        bookcase_books = Bookcase_book.objects.filter(
            bookcase_owner=owner, book__approved=True, book__deleted=False)
        selected_owner = get_object_or_404(User, id=owner)

        # To add pagination, show 9 books per page
        paginator = Paginator(bookcase_books, 9)

        page_number = request.GET.get('page')
        bookcase_books = paginator.get_page(page_number)

        return render(
            request,
            "bookcase_detail.html",
            {
                "books": bookcase_books,
                "bc_owner": selected_owner,
            },
        )
