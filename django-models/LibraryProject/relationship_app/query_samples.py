from relationship_app.models import Author, Book, Library, Librarian

# Query all books by a specific author
author = Author.objects.get(name="J.K. Rowling")
books_by_author = author.books.all()
print("Books by", author.name)
for book in books_by_author:
    print("-", book.title)

# List all books in a library
library = Library.objects.get(name="Central Library")
library_books = library.books.all()
print("\nBooks in", library.name)
for book in library_books:
    print("-", book.title)

# Retrieve the librarian for a library
librarian = library.librarian
print("\nLibrarian of", library.name, "is", librarian.name)
