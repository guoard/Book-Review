from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    def __str__(self):
        return f'{self.last_name} - {self.first_name}'


class Book(models.Model):
    class BookLanguage(models.TextChoices):
        PERSIAN = 'FA', 'Persian'
        ENGLISH = 'EN', 'English'

    title = models.CharField(max_length=200)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True, related_name='books')
    summary = models.TextField()
    genre = models.ManyToManyField(Genre)
    language = models.CharField(max_length=2, default=BookLanguage.PERSIAN, choices=BookLanguage.choices)
    liked_user = models.ManyToManyField(User, related_name='likes', blank=True)
    # TODO: implement image field

    def __str__(self):
        return self.title


class Wishlist(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    wished_book = models.ManyToManyField(Book)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'wishlist of {self.user}'
