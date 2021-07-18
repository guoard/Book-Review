from django.urls import path
from .views import BookList, BookDetail, BookCreate, like_book, LikedBookList

app_name = 'books'
urlpatterns = [
   path('list/', BookList.as_view(), name='book_list'),
   path('create/', BookCreate.as_view(), name='book_create'),
   path('detail/<int:pk>/', BookDetail.as_view(), name='book_detail'),
   path('like/<int:book_id>/', like_book, name='book_like'),
   path('likes/', LikedBookList.as_view(), name='book_liked')
]
