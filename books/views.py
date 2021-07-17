from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.permissions import AllowAny
from .permissions import IsStaffOrReadOnly
from .serializers import BookSerializer, DetailBookSerializer
from .models import Book


class BookList(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = (AllowAny,)
    filterset_fields = ['author', 'genre']
    search_fields = ['title']


class BookCreate(CreateAPIView):
    serializer_class = DetailBookSerializer
    permission_classes = (IsStaffOrReadOnly,)


class BookDetail(RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = DetailBookSerializer
    permission_classes = (IsStaffOrReadOnly,)
