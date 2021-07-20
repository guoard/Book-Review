from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework import generics
from rest_framework import status
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import AllowAny, IsAdminUser
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import User
from .serializers import UserSerializer, ListUserSerializer, UserWishlistSerializer
from books.models import Book


class LogoutAPIView(APIView):
    def get(self, request):
        # simply delete the token to force a login
        request.user.auth_token.delete()
        return Response(status=status.HTTP_200_OK)


class UserRegistration(generics.CreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = (AllowAny,)


class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer
    permission_classes = (IsAdminUser,)

    @method_decorator(cache_page(60))
    def dispatch(self, *args, **kwargs):
        return super(UserList, self).dispatch(*args, **kwargs)


class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = ListUserSerializer
    permission_classes = (IsAdminUser,)


class UserWishlist(APIView):
    permission_classes = (IsAdminUser,)

    def get(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        wished_book = user.wishlist.all()
        serializer = UserWishlistSerializer(wished_book, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        book_id = request.data.get('id')
        book = get_object_or_404(Book, pk=book_id)
        book.wished_users.add(user)
        return Response({'message': f'book added to {user.username}\'s wishlist'}, status=status.HTTP_201_CREATED)

    def delete(self, request, user_id):
        user = get_object_or_404(User, pk=user_id)
        book_id = request.data.get('id')
        book = get_object_or_404(Book, pk=book_id)
        book.wished_users.remove(user)
        return Response({'message': f'book removed from {user.username}\'s wishlist'})
