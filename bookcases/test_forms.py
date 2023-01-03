from django.test import TestCase
from .forms import SubmitForm


class TestItemForm(TestCase):

    def test_title_is_required(self):
        form = SubmitForm({'title': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('title', form.errors.keys())
        self.assertEqual(form.errors['title'][0], 'This field is required.')

    def test_author_is_required(self):
        form = SubmitForm({'author': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('author', form.errors.keys())
        self.assertEqual(form.errors['author'][0], 'This field is required.')

    def test_excerpt_is_required(self):
        form = SubmitForm({'excerpt': ''})
        self.assertFalse(form.is_valid())
        self.assertIn('excerpt', form.errors.keys())
        self.assertEqual(form.errors['excerpt'][0], 'This field is required.')

    def test_image_is_not_required(self):
        form = SubmitForm({'title': 'Say hello', 'author': 'Merel', 'excerpt': 'best book ever'})
        self.assertTrue(form.is_valid())

    def test_fields_are_explicit_in_form_metaclass(self):
        form = SubmitForm()
        self.assertEqual(form.Meta.fields, ('title', 'author', 'excerpt', 'featured_image'))