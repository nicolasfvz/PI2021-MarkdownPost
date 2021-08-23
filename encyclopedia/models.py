from django.db import models

# Create your models here.

class Posts(models.Model):
    """This class represent the Posts Table in the Database
    """
    title = models.CharField(max_length=255, unique=True)
    post = models.TextField()

    def __str__(self):
        """The __str__ method in Python represents the class objects as a string

        Returns:
            [str]: title
        """
        return f"{self.title}"

    def json(self):
        """Information about the object

        Returns:
            [JSON]: Returns the information in JSON of this object
        """
        return {
            'title' : self.title,
            'post'  : self.post
        }

class Users(models.Model):
    """This class represent the User Table in the Database
    """
    name = models.CharField(max_length=255, unique=False)
    password = models.CharField(max_length=255, unique=False)
    posts = models.ManyToManyField(Posts, blank=True, related_name="users")

    def json(self):
        """Information about the object

        Returns:
            [JSON]: Returns the information in JSON of this object
        """
        return {
            'name' : self.name,
            'posts'  : self.posts
        }

    def __str__(self):
        """The __str__ method in Python represents the class objects as a string

        Returns:
            [str]: title
        """
        return f"{self.name}"