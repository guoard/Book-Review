from django.db import models
from django.contrib.auth import get_user_model
from location_field.models.plain import PlainLocationField

User = get_user_model()


class Genre(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class Author(models.Model):
    first_name = models.CharField(max_length=200)
    last_name = models.CharField(max_length=200)

    @property
    def fullname(self):
        return f'{self.first_name} {self.last_name}'

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
    liked_users = models.ManyToManyField(User, related_name='likes', blank=True)
    wished_users = models.ManyToManyField(User, related_name='wishlist', blank=True)

    photo1 = models.ImageField(upload_to='book_images/%Y/%m/%d/', null=True, blank=True)
    photo2 = models.ImageField(upload_to='book_images/%Y/%m/%d/', null=True, blank=True)

    location = PlainLocationField(zoom=7, null=True)

    def __str__(self):
        return self.title
