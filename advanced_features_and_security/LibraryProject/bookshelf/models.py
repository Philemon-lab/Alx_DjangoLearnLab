from django.db import models

# Create your models here.
from django.contrib.auth import get_user_model

User = get_user_model()

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    published_date = models.DateField()
    added_by = models.ForeignKey(User, on_delete=models.CASCADE)
    
    class Meta:
        permissions = [
            ("can_add_book", "Can add book"),
            ("can_change_book", "Can edit book"),
            ("can_delete_book", "Can delete book"),
        ]

    def __str__(self):
        return self.title
