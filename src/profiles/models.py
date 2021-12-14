from django.db import models
from django.contrib.auth.models import User
from itertools import chain
import random

# Create your models here.

class Profile(models.Model):
    """This class represents a profile in the database. To create this class you need just a User(within the Django authentication system), other things are generated by default.
    """
    
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to='media/avatars/')
    background = models.ImageField(upload_to='media/backgrounds/', default='background.jpg')
    following = models.ManyToManyField(User, related_name='following', blank=True)
    bio = models.TextField(default="no bio...")
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        """The __str__ method in Python represents the class objects as a string

        Returns:
            [str]: Username of that user
        """
        return str(self.user)

    def get_my_post(self):
        """This funcion is called when you want all of your post

        Returns:
            [QuerySet]: Uses a releted_name to call all items in the table Post that you are the author \posts\models.py
        """
        return self.posts.all()
    
    @property
    def num_post(self):
        """Count all your post

        Returns:
            [int]: The number of posts that a profile have
        """
        return self.posts.all().count()
    
    def get_following(self):
        """Get all profiles that you are following

        Returns:
            [list[QuerySet]]: Everyone that you are following
        """
        return self.following.all()
    
    @property
    def following_count(self):
        """Get the number of profiles that you are following

        Returns:
            [int]: Number of profiles that you are following duh
        """
        return self.get_following().count()
    
    
    def get_following_users(self):
        """Get all profiles that you are following

        Returns:
            [list[User]]: Everyone that you are following
        """
        following_list = [p for p in self.get_following()]
        return following_list
    
    def get_my_and_following_posts(self):
        """Get all my post, and the post of the profiles that I'm following

        Returns:
            [QuerySet]: With all the post, mine and the profiles that I'm in cresending order by the time they were created
        """
        users = [ user for user in self.get_following()]
        posts = []
        qs = None
        for u in users:
            p = Profile.objects.get(user=u)
            p_posts = p.posts.all()
            posts.append(p_posts)
        my_post = self.posts.all()
        posts.append(my_post)
        if len(posts) > 0:
            qs = sorted(chain(*posts), reverse=True, key=lambda obj: obj.created)
        return qs
    
    def get_proposals_for_following(self):
        """Get proposals for profiles to follow

        Returns:
            [list[QuerySet]]: A list of three random options you to follow
        """
        profiles = Profile.objects.all().exclude(user=self.user)
        followers_list = [p for p in self.get_following()]
        available = [p.user for p in profiles if p.user not in followers_list]
        random.shuffle(available)
        return available[:3]
    
    def get_followers(self):
        """Get all profiles that follow you

        Returns:
            [list[QuerySer]]: All of your followers
        """
        qs = Profile.objects.all()
        followers_list = []
        for profile in qs:
            if self.user in profile.get_following():
                followers_list.append(profile)
        return followers_list
    
    @property
    def followers_count(self):
        """Count how many followers you have
        

        Returns:
            [int]: The number of followers that you have
        """
        return len(self.get_followers())
