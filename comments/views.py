from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated, AllowAny
from rest_framework.views import APIView
from rest_framework import generics, status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from books.permissions import IsStaffOrReadOnly
from .models import Comment
from .serializers import ListCommentSerializer, CreateCommentSerializer
from books.models import Book


# class CommentAPIView(APIView):
#     permission_classes = (AllowAny,)
#
#     def get(self, request, book_id):
#         book = get_object_or_404(Book, pk=book_id)
#         comments = Comment.objects.filter(book=book)
#         comments_serializer = ListCommentSerializer(comments, many=True)
#         return Response(comments_serializer.data)


class ListComment(generics.ListAPIView):
    permission_classes = (AllowAny,)
    serializer_class = ListCommentSerializer

    def get_queryset(self):
        book_id = self.kwargs.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        order_by = self.request.query_params.get('order_by', '-created')
        queryset = Comment.objects.filter(book=book)

        return queryset.order_by(order_by)
# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_comment(request, book_id):
#     book = get_object_or_404(Book, pk=book_id)
#     serializer = CreateCommentSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save(author=request.user, book=book)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CreateComment(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CreateCommentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        book_id = self.kwargs.get('book_id')
        book = get_object_or_404(Book, pk=book_id)
        serializer.save(author=self.request.user, book=book)
