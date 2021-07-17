from django.db import models
from django.contrib.auth import get_user_model

from books.models import Book

User = get_user_model()


class CommentManager(models.Manager):
    def related_comments_to_book(self, book):
        return self.filter(book=book)


class Comment(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    start_time_reading = models.DateField()
    end_time_reading = models.DateField()
    approved = models.BooleanField(default=False)

    objects = CommentManager()

    class Meta:
        ordering = ['-created']

    @property
    def read_duration(self):
        return self.end_time_reading - self.start_time_reading

    def __str__(self):
        return f"{self.author} commented for {self.book}"
