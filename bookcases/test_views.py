from django.test import TestCase
from django.shortcuts import reverse
from django.contrib.auth.models import User
from .models import Book, Bookcase_book


class TestViews(TestCase):
    def setUp(self):
        self.testuser = User.objects.get_or_create(username='testuser')
        self.client.force_login(self.testuser[0])
        self.tbook = Book.objects.create(title='Testbook', author='Tester', excerpt='testing')
        self.tbookcase_book = Bookcase_book.objects.create(bookcase_owner=self.testuser[0], book=self.tbook)

    def test_get_book_list_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_visit_bookcases_page(self):
        response = self.client.get(f'/bookcase_detail/{self.tbookcase_book.bookcase_owner.id}')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookcase_detail.html')

    def test_get_user_bookcase_page(self):
        response = self.client.get('/user_bookcase/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_bookcase.html')
    
    # def test_get_book_detail_page(self):
    #     print(self.tbook.slug)
    #     response = self.client.get(f'slug:{self.tbook.slug}')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'book_detail.html')

    def test_get_submit_book_page(self):
        response = self.client.get('/submit_book/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_book.html')

    def test_can_add_book(self):
        response = self.client.post('/submit_book/', {'title': 'Testbook2', 'author':'Esther Tester', 'excerpt': 'testing twice'})
        self.assertRedirects(response, '/submit_book/')
        added_book = Book.objects.filter(title='Testbook2')
        self.assertEqual(len(added_book), 1)

    def test_can_delete_bookcase_book(self):
        book = Book.objects.create(title='Testbook3', author='Tester', excerpt='testing')
        bookcase_book = Bookcase_book.objects.create(bookcase_owner=self.testuser[0], book=self.tbook)
        response = self.client.get(f'/delete/{book.id}')
        delete_bc_book = Bookcase_book.objects.filter(book=book.id)
        self.assertEqual(len(delete_bc_book), 0)
        
    # def test_can_change_category(self):

# NOT TESTABLE - this results in error because DISTINCT IS NOT SUPPORTED
    # def test_get_bookcases_page(self):
    #     response = self.client.get('/bookcases/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'bookcases.html')