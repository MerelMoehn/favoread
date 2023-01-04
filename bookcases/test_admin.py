from django.test import TestCase
from django.contrib import admin
from django.shortcuts import reverse
from django.contrib.admin.sites import AdminSite
from django.contrib.auth.models import User
from .admin import BookAdmin
from .models import Book


class TestAdmin(TestCase):
    def setUp(self):
        self.admin = User.objects.create_superuser(username='admin')
        self.client.force_login(self.admin)
        self.book = Book.objects.create(title='Testbook', author='Tester', excerpt='testing')

    def test_approve_true_by_admin(self):
        response = self.client.post('admin:bookcases_book_changelist', {'_selected_action': 'approve_books'})
        self.assertTrue(self.book.approved)
