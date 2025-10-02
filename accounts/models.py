from random import choices
from django.conf import settings
from django.contrib.auth.models import User
from django.db import models


class Profile(models.Model):
    GENDER_CHOICES = [
        ("male", "Male"),
        ("female", "Female"),
        ("other", "Other"),
    ]
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="profile")
    first_name = models.CharField(max_length=150, blank=True)
    last_name = models.CharField(max_length=150, blank=True)
    gender = models.CharField(max_length=10, blank=True, choices=GENDER_CHOICES)
    region = models.CharField(max_length=50, blank=True)
    language = models.CharField(max_length=5, default="en")

    def __str__(self):
        return f"Profile({self.user.username})"




