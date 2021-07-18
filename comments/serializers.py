from django.contrib.auth import get_user_model
from rest_framework import serializers

from .models import Comment

User = get_user_model()


class ListCommentSerializer(serializers.ModelSerializer):
    read_duration = serializers.ReadOnlyField()
    created_at = serializers.ReadOnlyField()

    class Meta:
        model = Comment
        fields = ['author', 'content', 'start_time_reading', 'end_time_reading', 'read_duration', 'created_at']


class CreateCommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['content', 'start_time_reading', 'end_time_reading']

    def validate(self, data):
        if data['start_time_reading'] >= data['end_time_reading']:
            raise serializers.ValidationError({"end_time_reading": "finish time must occur after start time"})
        return data
