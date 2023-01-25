import uuid
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User

# Create your models here.


class Genre(models.Model):

    name = models.CharField(max_length=150)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("catalog:book_detail", kwargs={"pk": self.pk})

# If I want to expand another language


class Language(models.Model):

    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name

    class Meta:
        db_table = ''
        managed = True
        verbose_name = 'Language'
        verbose_name_plural = 'Languages'


class Book(models.Model):

    title = models.CharField(max_length=50)
    author = models.ForeignKey(
        'Author', on_delete=models.SET_NULL, null=True)
    summary = models.TextField(max_length=500)
    isbn = models.CharField('ISBN', max_length=13, unique=True)
    genre = models.ManyToManyField(Genre)

    language = models.ForeignKey(
        "Language", on_delete=models.SET_NULL, null=True)

    def __str__(self):
        return '{} - {} '.format(self.title, self.author, self.genre)

    def get_absolute_url(self):
        return reverse("catalog:book_detail", kwargs={"pk": self.pk})


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    date_of_birth = models.DateField(blank=True, null=True)

    class Meta:
        ordering = ['last_name', 'first_name']

    def __str__(self):
        return f'{self.first_name}, {self.last_name}'

    def get_absolute_url(self):
        return reverse("catalog:author_detail", kwargs={"pk": self.pk})


class BookInstance(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    book = models.ForeignKey("Book", on_delete=models.RESTRICT, null=True)
    imprint = models.CharField(max_length=200)
    due_back = models.DateField(blank=True, null=True)
    borrower = models.ForeignKey(
        User, on_delete=models.SET_NULL, blank=True, null=True)

    LOAN_STATUS = (
        ('m', 'Maintenance'),
        ('o', 'On Loan'),
        ('a', 'Available'),
        ('r', 'Reserved')
    )

    status = models.CharField(
        max_length=1, choices=LOAN_STATUS, blank=True, default='m')

    class Meta:
        ordering = ['due_back']

    def __str__(self):
        return f'{self.id} - {self.book.title}'

    def get_absolute_url(self):
        return reverse("catalog:bookInstance_detail", kwargs={"pk": self.pk})


class User(models.Model):
    username = models.CharField(max_length=50)

    def __str__(self):
        return self.username
