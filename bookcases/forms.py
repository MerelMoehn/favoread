from .models import Book
from django import forms


class SubmitForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('title', 'author', 'excerpt', 'featured_image')
