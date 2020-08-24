from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.us.forms import USSocialSecurityNumberField


class CustomUser(AbstractUser):

    class UserRoles(models.TextChoices):
        USER = 'user'
        ADMIN = 'admin'

    role = models.CharField(choices=UserRoles.choices, max_length=64)
    SSN = models.CharField(max_length=11, validators = [USSocialSecurityNumberField.clean])
