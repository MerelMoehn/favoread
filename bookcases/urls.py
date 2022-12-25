from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('get_inspired/', views.BookcaseOwners.as_view(), name='get_inspired'),
    path('submit_book/', views.SubmitBook.as_view(), name='submit_book'),
    path('user_bookcase/', views.UserBookcase.as_view(), name="user_bookcase"),
    path('<slug:slug>/', views.BookDetail.as_view(), name='book_detail'),
    path('add/<slug:slug>/', views.AddBook.as_view(), name='add_book')
]
