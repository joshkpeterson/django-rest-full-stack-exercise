from django.contrib.auth.models import AbstractUser
from django.db import models


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
    # SSN = USSocialSecurityNumberField()
    roles = models.ManyToManyField(Role)