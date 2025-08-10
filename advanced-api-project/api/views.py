from django.shortcuts import render
from rest_framework import generics, permissions
from .models import Book
from .serializers import BookSerializer

# List all books
class BookListView(generics.ListAPIView):
    """
    Retrieves a list of all books.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Retrieve a single book
class BookDetailView(generics.RetrieveAPIView):
    """
    Retrieves details of a single book by ID.
    Accessible to everyone (read-only).
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.AllowAny]


# Create a new book
class BookCreateView(generics.CreateAPIView):
    """
    Allows authenticated users to create a new book.
    Validates publication_year before saving.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Update an existing book
class BookUpdateView(generics.UpdateAPIView):
    """
    Allows authenticated users to update book details.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]


# Delete a book
class BookDeleteView(generics.DestroyAPIView):
    """
    Allows authenticated users to delete a book.
    """
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [permissions.IsAuthenticated]
