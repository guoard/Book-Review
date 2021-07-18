from datetime import datetime

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
        return (self.end_time_reading - self.start_time_reading).days

    @property
    def created_at(self):
        time = datetime.now()
        if self.created.day == time.day:
            return f'{time.hour - self.created.hour} hours ago'
        elif self.created.month == time.month:
            return f'{time.day - self.created.day} days ago'
        elif self.created.year == time.year:
            return f'{time.month - self.created.month} months ago'
        else:
            return f'{time.year - self.created.year} years ago'

    def __str__(self):
        return f"{self.author} commented for {self.book}"
