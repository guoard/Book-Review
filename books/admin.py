from django.contrib import admin
from .models import Book, Genre, Author, Wishlist


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    pass


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    pass


@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass


@admin.register(Wishlist)
class WishlistAdmin(admin.ModelAdmin):
    pass
