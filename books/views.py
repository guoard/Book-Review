from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response

from .permissions import IsStaffOrReadOnly
from .serializers import BookSerializer, DetailBookSerializer, LikedBookSerializer
from .models import Book


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['author', 'genre']
    search_fields = ['title']


class BookCreate(CreateAPIView):
    serializer_class = DetailBookSerializer
    permission_classes = (IsAdminUser,)


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = DetailBookSerializer
    permission_classes = (IsStaffOrReadOnly,)


@api_view(['POST'])
def like_book(request, book_id):
    """ API endpoint to like/disLike a post """
    book = get_object_or_404(Book, pk=book_id)
    if request.user in book.liked_users.all():
        book.liked_users.remove(request.user)
        book.save()
        return Response({'message': 'disliked successfully'}, status=status.HTTP_200_OK)
    else:
        book.liked_users.add(request.user)
        book.save()
        return Response({'message': 'liked successfully'}, status=status.HTTP_200_OK)


class LikedBookList(ListAPIView):
    serializer_class = LikedBookSerializer

    def get_queryset(self):
        books = Book.objects.filter(liked_users=self.request.user)
        return books
