from django.contrib import admin
from .models import Author, Book, Genre, Language, BookInstance

# Register your models here.
admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Genre)
admin.site.register(Language)
admin.site.register(BookInstance)
