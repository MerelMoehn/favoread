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
        data = {'action': 'approve_books', '_selected_action': self.book.id}
        change_url = reverse('admin:bookcases_book_changelist')
        # POST data to change_url
        response = self.client.post(change_url, data, follow=True)
        
        self.book.refresh_from_db()
        self.assertTrue(self.book.approved)
