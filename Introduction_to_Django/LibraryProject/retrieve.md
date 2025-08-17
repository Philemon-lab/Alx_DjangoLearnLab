
---

### **retrieve.md**

```markdown
# Retrieve Operation

```python
from bookshelf.models import Book

# Retrieve the book by title
Book.objects.get(title="1984")
#Output
<Book: 1984>