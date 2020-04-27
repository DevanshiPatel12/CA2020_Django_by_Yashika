from django.db import models
AUTH_USER_MODEL='users.CustomUser'
AUTH_USER_MODEL='users.CustomUser'
from django.contrib.auth.models import AbstractUser

#from django.contrib.auth import get_user_model
#from django.conf import settings

# Create your models here.
class CustomUser(AbstractUser):
    pass