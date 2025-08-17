import os
import django

# Setup Django environment
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'LibraryProject.settings')
django.setup()

from bookshelf.models import Book

# Create a book
book1 = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

print(f"Book created: {book1}")
