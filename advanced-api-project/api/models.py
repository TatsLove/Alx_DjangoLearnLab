from django.db import models
from django.utils import timezone

class Author(models.Model):
    """
    Represents a book author.
    - name: Name of the author.
    - Relationship: One author can have many books.
    """
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name


class Book(models.Model):
    """
    Represents a book.
    - title: Title of the book.
    - publication_year: Year the book was published.
    - author: ForeignKey to Author, linking books to their author.
    """
    title = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
