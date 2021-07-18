from rest_framework import serializers
from .models import Book


class AuthorField(serializers.RelatedField):
    def to_representation(self, value):
        return value.fullname


class GenreField(serializers.RelatedField):
    def to_representation(self, value):
        return value.name


class UserField(serializers.RelatedField):
    def to_representation(self, value):
        return value.username


class BookSerializer(serializers.ModelSerializer):
    author = AuthorField(read_only=True)
    genre = GenreField(read_only=True, many=True)

    class Meta:
        model = Book
        exclude = ['liked_users', 'wished_users']


class DetailBookSerializer(serializers.ModelSerializer):
    liked_users = UserField(read_only=True, many=True)
    author = AuthorField(read_only=True)
    genre = GenreField(read_only=True, many=True)
    likes_count = serializers.SerializerMethodField()

    class Meta:
        model = Book
        exclude = ['wished_users']

    def get_likes_count(self, obj):
        return obj.liked_users.count()
