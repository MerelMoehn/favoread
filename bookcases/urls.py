from . import views
from django.urls import path

urlpatterns = [
    path('', views.BookList.as_view(), name='home'),
    path('get_inspired/', views.UserList.as_view(), name='get_inspired'),
    path('submit_book/', views.SubmitBook.as_view(), name='submit_book'),
    path('bookcase_detail/', views.BookcaseList.as_view(), name='bookcase_detail'),
]
