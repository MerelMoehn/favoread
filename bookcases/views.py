from django.shortcuts import render, get_object_or_404
from django.views import generic, View
from .models import Book, Bookcase, Bookcase_book
from django.contrib.auth.models import User
from .forms import SubmitForm


class BookList(generic.ListView):
    model = Book
    queryset = Book.objects.filter(approved=True).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class UserList(generic.ListView):
    model = User
    queryset = User.objects.all()
    template_name = 'get_inspired.html'
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

        # to check whether user has a bookcase already, if not, create a Bookcase instance
            owner = request.user.id
            try:
                user_bookcase = bookcase.filter(owner=owner)
        
            except ObjectDoesNotExist:
                Bookcase.objects.create(owner=request.user)

        # to add the book as an instance to the Bookcase_book model
            bookcase_book = Bookcase_book.objects.create(book_id=new_book)

        else:
            submit_form = SubmitForm()

        return render(
            request,
            "submit_book.html",
        )


class BookcaseList(generic.ListView):
    model = Bookcase()
    queryset = Bookcase.objects.order_by('-created_on')
    template_name = 'bookcase_detail.html'
    paginate_by = 6
