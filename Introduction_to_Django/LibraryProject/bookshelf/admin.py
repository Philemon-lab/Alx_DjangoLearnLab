from django.contrib import admin
from .models import Book

# Create a custom admin class for Book
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')  # Columns shown in list view
    search_fields = ('title', 'author')                     # Add search box for title and author
    list_filter = ('publication_year',)                     # Filter by publication year

# Register Book with the custom admin
admin.site.register(Book, BookAdmin)
