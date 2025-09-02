from django.db import models

class Author(models.Model):
<<<<<<< HEAD
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Book(models.Model):
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, related_name="books", on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.title} ({self.publication_year})"
=======
    """
    Author model representing a book author.
    Fields:
    - name: CharField to store the author's name (max 100 characters)
    """
    name = models.CharField(max_length=100)
    
    def __str__(self):
        return self.name

class Book(models.Model):
    """
    Book model representing a published book.
    Fields:
    - title: CharField for the book's title (max 200 characters)
    - publication_year: IntegerField for the year of publication
    - author: ForeignKey linking to Author model (one-to-many relationship)
              When an author is deleted, their books are also deleted (CASCADE)
    """
    title = models.CharField(max_length=200)
    publication_year = models.IntegerField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')
    
    def __str__(self):
        return f"{self.title} by {self.author.name}"
>>>>>>> f408c826089a138d6b665aa4177820c10113a8bc
