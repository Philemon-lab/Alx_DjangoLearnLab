from django.shortcuts import render
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

# List all books OR create a new one
class BookListCreate(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

# Retrieve, update, or delete a single book
class BookDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
