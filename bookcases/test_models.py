from django.test import TestCase
from .models import Book, Bookcase_book
from django.contrib.auth.models import User


class TestModels(TestCase):
    def setUp(self):
        self.testuser = User.objects.get_or_create(username='testuser')
        self.tbook = Book.objects.create(title='Testbook', author='Tester', excerpt='testing')
        self.tbc_book = Bookcase_book.objects.create(bookcase_owner=self.testuser[0], book=self.tbook)

    def test_bookcase_book_default_0(self):
        self.assertTrue(self.tbc_book.status == 0)
    
    def test_book_default_notapproved(self):
        self.assertFalse(self.tbook.approved)

    def test_book_string_method_returns_name(self):
        self.assertEqual(str(self.tbook), "Testbook by Tester")

    def test_tbcbook_string_method_returns_name(self):
        self.assertEqual(str(self.tbc_book), "Testbook by Tester in testuser's bookcase")