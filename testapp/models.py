from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.signals import user_logged_in

# Create your models here.
class User(AbstractUser):
    employee_id = models.CharField(max_length=128, unique=True, blank=True, null=True)
    login_count = models.PositiveIntegerField(default=0)

# Increments the login count of the user every time he logs in
def login_user(sender, request, user, **kwargs):
    user.login_count = user.login_count + 1
    user.save()

user_logged_in.connect(login_user)
