from django.db import models
from django.contrib.auth.models import User
from profiles.models import Profile

# Create your models here.

class Post(models.Model):
    """This class represent the Posts Table in the Database
    """
    title = models.CharField(max_length=255)
    body = models.TextField()
    liked = models.ManyToManyField(User, default=None, blank=True)
    author = models.ForeignKey(Profile, on_delete=models.CASCADE, null=True, related_name='posts')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """The __str__ method in Python represents the class objects as a string

        Returns:
            [str]: title
        """
        return f"{self.title}"

    @property
    def get_liked(self):
        return self.liked.all()

    def like_count(self):
        return self.liked.all().count()

    def json(self):
        """Information about the object

        Returns:
            [JSON]: Returns the information in JSON of this object
        """
        return {
            'title' : self.title,
            'post'  : self.post
        }