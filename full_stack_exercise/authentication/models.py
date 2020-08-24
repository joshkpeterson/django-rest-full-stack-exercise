from django.contrib.auth.models import AbstractUser
from django.db import models
from localflavor.us.forms import USSocialSecurityNumberField


class Role(models.Model):
    USER = 1
    ADMIN = 2
    ROLE_CHOICES = (
        (USER, 'user'),
        (ADMIN, 'admin'),
    )

    id = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()


class CustomUser(AbstractUser):
    USER_ROLE_CHOICES = (
        (1, 'user'),
        (2, 'admin'),
    )

    role = models.PositiveSmallIntegerField(choices=USER_ROLE_CHOICES)
    SSN = models.CharField(max_length=11, validators = [USSocialSecurityNumberField.clean])

