from .models import Book
from django import forms

# This Form is used to let user submit a book


class SubmitForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'excerpt', 'featured_image')
