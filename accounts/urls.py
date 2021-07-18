from django.urls import path
from rest_framework.authtoken.views import obtain_auth_token

from .views import UserRegistration, LogoutAPIView, UserList, UserDetail, UserWishlist

urlpatterns = [
    path('login/', obtain_auth_token),
    path('logout/', LogoutAPIView.as_view()),
    path('register/', UserRegistration.as_view()),
    path('users/', UserList.as_view(), name='user-list'),
    path('users/<int:pk>', UserDetail.as_view(), name='user-detail'),
    path('users/<int:user_id>/wishlist', UserWishlist.as_view(), name='user-wishlist')

]