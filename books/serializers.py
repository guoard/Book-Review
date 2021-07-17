from rest_framework.serializers import ModelSerializer, RelatedField
from .models import Book, Author, Genre


class AuthorField(RelatedField):
    def to_representation(self, value):
        return value.fullname


class GenreField(RelatedField):
    def to_representation(self, value):
        return value.name


class BookSerializer(ModelSerializer):
    author = AuthorField(read_only=True)
    genre = GenreField(read_only=True, many=True)

    class Meta:
        model = Book
        exclude = ('liked_user',)


class DetailBookSerializer(ModelSerializer):
    class Meta:
        model = Book
        exclude = ('liked_user',)