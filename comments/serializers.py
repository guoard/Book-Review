from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment
from books.models import Book

User = get_user_model()


class ListCommentSerializer(serializers.ModelSerializer):
    read_duration = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ['author', 'content', 'start_time_reading', 'end_time_reading', 'read_duration']


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'start_time_reading', 'end_time_reading']
