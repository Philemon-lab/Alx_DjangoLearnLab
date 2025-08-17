# Task 2: Utilizing the Django Admin Interface

## Objective
Gain practical experience with the Django admin interface by configuring the admin to manage the `Book` model.  
This task demonstrates how to use Django’s built-in admin interface to efficiently perform data management tasks.

---

## Steps Completed

### 1. Registered the Book Model with the Admin
In `bookshelf/admin.py`:
```python
from django.contrib import admin
from .models import Book

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns in list view
    search_fields = ('title', 'author')                     # Search by title and author
    list_filter = ('publication_year',)                     # Filter by publication year
