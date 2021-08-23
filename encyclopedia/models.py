from django.db import models

# Create your models here.

class Posts(models.Model):
    title = models.CharField(max_length=255, unique=True)
    post = models.TextField()

    def __str__(self):
        return f"{self.title}"

    def json(self):
        return {
            'title' : self.title,
            'post'  : self.post
        }

class Users(models.Model):
    name = models.CharField(max_length=255, unique=False)
    password = models.CharField(max_length=255, unique=False)
    posts = models.ManyToManyField(Posts, blank=True, related_name="users")

    def json(self):
        return {
            'name' : self.name,
            'posts'  : self.posts
        }

    def __str__(self):
        return f"{self.name}"