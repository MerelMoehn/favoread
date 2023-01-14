from django.test import TestCase
from django.shortcuts import reverse, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.messages import get_messages
from .models import Book, Bookcase_book


class TestViews(TestCase):
    # Setup: Create & Login User, and create Book and Bookcase_book instance
    def setUp(self):
        self.testuser = User.objects.get_or_create(username='testuser')
        self.client.force_login(self.testuser[0])
        self.tbook = Book.objects.create(title='Testbook', author='Tester',
                                         excerpt='testing')
        self.tbookcase_book = Bookcase_book.objects.create(
            bookcase_owner=self.testuser[0],
            book=self.tbook)

    def test_get_book_list_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_get_visit_bookcases_page(self):
        response = self.client.get(
            f'/bookcase_detail/{self.tbookcase_book.bookcase_owner.id}'
            )
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'bookcase_detail.html')

    def test_get_user_bookcase_page(self):
        response = self.client.get('/user_bookcase/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_bookcase.html')

    def test_get_book_detail_page(self):
        self.tbook.approved = True
        self.tbook.save()
        response = self.client.get(f'/{self.tbook.slug}/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'book_detail.html')

    def test_get_submit_book_page(self):
        response = self.client.get('/submit_book/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_book.html')

    def test_add_book_to_bookcase(self):
        book = Book.objects.create(title='Add to Bookcase', author='TestMe',
                                   excerpt='testing')

        response = self.client.post(f'/add/{book.slug}/')

        book_in_bookcase = Bookcase_book.objects.filter(
            book=book.id,
            bookcase_owner=self.testuser[0].id)
        self.assertEqual(len(book_in_bookcase), 1)

    def test_add_book_twice_throws_error(self):
        response = self.client.post(f'/add/{self.tbook.slug}/')

        # Based on StackOverflow for code to check for messages
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn('This book is already in your bookcase', messages)

    def test_can_submit_book(self):
        response = self.client.post('/submit_book/',
                                    {'title': 'Testbook2',
                                     'author': 'Esther Tester',
                                     'excerpt': 'testing twice'})

        self.assertRedirects(response, '/submit_book/')

        added_book = Book.objects.filter(title='Testbook2')
        self.assertEqual(len(added_book), 1)

    def test_submit_book_throws_error(self):
        response = self.client.post('/submit_book/',
                                    {'title': '',
                                     'author': 'Esther Tester',
                                     'excerpt': 'testing twice'})

        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            'Oeps, something went wrong. Maybe this title already exists.',
            messages)

    def test_can_change_status(self):
        response = self.client.post(f'/update_status/{self.tbook.id}/',
                                    {'status': 2}, follow=True)

        self.assertRedirects(response, reverse('user_bookcase'),
                             target_status_code=200)

        self.tbookcase_book.refresh_from_db()
        self.assertFalse(self.tbookcase_book.status == 0)

    def test_can_delete_bookcase_book(self):
        book = Book.objects.create(title='Testbook3',
                                   author='Tester', excerpt='testing')
        bc_book = Bookcase_book.objects.create(bookcase_owner=self.testuser[0],
                                               book=book)

        response = self.client.post(f'/delete/bookcase/{book.id}/')

        delete_bc_book = Bookcase_book.objects.filter(book=book.id)
        self.assertEqual(len(delete_bc_book), 0)

    def test_can_delete_book(self):
        response = self.client.post(f'/delete_book/{self.tbook.id}/')

        book = get_object_or_404(Book, id=self.tbook.id)
        book.refresh_from_db()
        messages = [m.message for m in get_messages(response.wsgi_request)]
        self.assertIn(
            'The book has been deleted.',
            messages)
        self.assertRedirects(response, '/')
        self.assertTrue(book.deleted)


# NOT TESTABLE - this results in error because DISTINCT IS NOT
#  SUPPORTED in local DB
#     def test_get_bookcases_page(self):
#         response = self.client.get('/bookcases/')
#         self.assertEqual(response.status_code, 200)
