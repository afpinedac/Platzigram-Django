"""Posts models"""

from django.db import models


class User(models.Model):
    """User model."""

    email = models.EmailField(unique=True)
    password = models.CharField(max_length=200)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    bio = models.TextField(blank=True)
    birth_date = models.DateField(blank=True, null=True)
    created = models.DateField(auto_now_add=True)
    modified = models.DateField(auto_now=True)
    is_admin = models.BooleanField(default=False)
