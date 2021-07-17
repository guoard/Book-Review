from django.urls import path
from .views import BookList, BookDetail, BookCreate

app_name = 'books'
urlpatterns = [
   path('list/', BookList.as_view(), name='book_list'),
   path('create/', BookCreate.as_view(), name='book_create'),
   path('detail/<int:pk>', BookDetail.as_view(), name='book_detail')
]
