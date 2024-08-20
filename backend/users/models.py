from django.db import models
from django.contrib.auth.models import (
    AbstractBaseUser,
    PermissionsMixin,
)

from rest_framework_simplejwt.tokens import RefreshToken
from .managers import UserManager
# Create your models here.

class User(AbstractBaseUser, PermissionsMixin):
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(max_length=255, unique=True)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    USERNAME_FIELD = "email"

    def tokens(self):
        refresh = RefreshToken.for_user(self)
        return {
            'refresh': str(refresh),
            'access': str(refresh.access_token)
        }