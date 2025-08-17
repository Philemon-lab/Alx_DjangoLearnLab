# Create Operation

```python
from bookshelf.models import Book

# Create a new Book instance
book1 = Book.objects.create(
    title="1984",
    author="George Orwell",
    publication_year=1949
)

# Check all books
Book.objects.all()
#Output 
<QuerySet [<Book: 1984>]>