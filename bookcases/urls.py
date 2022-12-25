from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('get_inspired/', views.BookcaseOwners.as_view(), name='get_inspired'),
    path('submit_book/', views.SubmitBook.as_view(), name='submit_book'),
    path('<slug:slug>/', views.BookDetail.as_view(), name='book_detail'),
    path('<slug:owner>/', views.BookcaseBookList.as_view(), name='bookcase_detail'),
]
