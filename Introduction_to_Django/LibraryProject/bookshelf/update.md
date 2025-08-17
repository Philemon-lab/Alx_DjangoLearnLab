
---

### **update.md**

```markdown
# Update Operation

```python
from bookshelf.models import Book

# Get the book instance
book = Book.objects.get(title="1984")

# Update the title
book.title = "Nineteen Eighty-Four"
book.save()

# Check the updated book
Book.objects.get(pk=book.pk)
# Output
<Book: Nineteen Eighty-Four>
