from django.urls import path

from .views import BookListApiView, BookDetailApiview, BookDeleteApiView, BookCreateApiView,BooksUpdateApiview, book_list_view





urlpatterns=[
    path('', BookListApiView.as_view(), ),
    path('books/create/', BookCreateApiView.as_view(), ),
    path('books/<int:pk>/', BookDetailApiview.as_view(), ),
    path('books/<int:pk>/update/',BooksUpdateApiview.as_view(), ),
    path('books/<int:pk>/delete', BookDeleteApiView.as_view(), ),
    # path('books/', book_list_view),

]