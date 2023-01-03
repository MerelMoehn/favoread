from django.test import TestCase
from django.contrib.auth.models import User


class TestViews(TestCase):
    def setUp(self):
        self.client.force_login(User.objects.get_or_create(username='testuser')[0])

    def test_get_book_list_page(self):
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

# NOT TESTABLE - this results in error because DISTINCT IS NOT SUPPORTED
    # def test_get_bookcases_page(self):
    #     response = self.client.get('/bookcases/')
    #     self.assertEqual(response.status_code, 200)
    #     self.assertTemplateUsed(response, 'bookcases.html')

    # def test_get_visit_bookcases_page(self):

    def test_get_user_bookcase_page(self):
        response = self.client.get('/user_bookcase/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'user_bookcase.html')
    
    # def test_get_book_detail_page(self):

    def test_get_submit_book_page(self):
        response = self.client.get('/submit_book/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'submit_book.html')
    
    # def test_can_add_book(self):

    # def test_can_delete_book(self):
    
    # def test_can_change_category(self):
