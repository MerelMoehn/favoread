from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('submit_book/', views.SubmitBook.as_view(), name='submit_book'),
    path('bookcases/', views.Bookcases.as_view(), name='bookcases'),
    path('user_bookcase/', views.UserBookcase.as_view(), name='user_bookcase'),
    # path('bookcase_detail/', views.VisitBookcase.as_view(), name='bookcase_detail'),
    path('<slug:slug>/', views.BookDetail.as_view(), name='book_detail'),
    path('delete/<book>/', views.DeleteBook.as_view(), name='delete_book'),
    path('update_status/<book>/', views.UpdateStatus.as_view(), name='update_status'),
    path('add/<slug:slug>/', views.AddBook.as_view(), name='add_book')
]
