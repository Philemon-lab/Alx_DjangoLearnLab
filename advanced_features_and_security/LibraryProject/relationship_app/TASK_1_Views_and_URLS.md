# Task 1: Django Views and URL Configuration

**Objective:**  
Develop proficiency in creating both function-based and class-based views in Django, and configuring URL patterns to handle web requests effectively.

---

## 1. Function-based View

File: `relationship_app/views.py`

```python
from django.shortcuts import render
from .models import Book

# Function-based view to list all books
def list_books(request):
    books = Book.objects.all()  # Fetch all books
    return render(request, 'relationship_app/list_books.html', {'books': books})
