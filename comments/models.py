from django.db import models
from django.contrib.auth import get_user_model

from books.models import Book

User = get_user_model()


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_time_reading = models.DateField()
    end_time_reading = models.DateField(blank=True, null=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created']

    def __str__(self):
        return f"{self.author} commented for {self.book}"
