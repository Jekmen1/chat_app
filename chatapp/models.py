from django.db import models
from django.contrib.auth.models import User

from django.contrib.auth.models import AbstractUser
from django.db import models

class Users(AbstractUser):
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        verbose_name='user permissions',
        blank=True,
        related_name='custom_user_permissions_set',
        related_query_name='user',
    )

    groups = models.ManyToManyField(
        'auth.Group',
        verbose_name='groups',
        blank=True,
        related_name='custom_user_groups_set',
        related_query_name='user',
    )

    def __str__(self):
        return self.username

class Room(models.Model):
    name = models.CharField(max_length=20)
    slug = models.SlugField(max_length=100)

    def __str__(self):
        return "Room : " + self.name + " | Id : " + self.slug


class Message(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Message is :- " + self.content
