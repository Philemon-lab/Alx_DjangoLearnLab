from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL


class Post(models.Model):   # ✅ Class name should be capitalized
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    title = models.CharField(max_length=255)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="likes")
    created_at = models.DateTimeField(auto_now_add=True)

class Meta:
    unique_together = ('user', 'post')
    
    def __str__(self):
        return self.title


class Comment(models.Model):   # ✅ Capitalized
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")  # ✅ reference Post, not posts
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Comment by {self.author} on {self.post}"
