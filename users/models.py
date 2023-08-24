from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.db import models

from base.models import NULLABLE
from users.services import LowerCaseEmailField


class User(AbstractUser):
    """User model"""
    username = models.CharField(_('username'), max_length=64, **NULLABLE)
    email = LowerCaseEmailField(_('email address'), unique=True)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return f'{self.email}'

    class Meta:
        verbose_name = 'user'
        verbose_name_plural = 'users'
