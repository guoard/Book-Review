from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()
from books.models import Book

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("username", "password")
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        return user


class ListUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserWishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ['id', 'title']
