from django.db import models

from django.contrib.auth.models import AbstractUser
from medic_back_login.utils.models import MedicBaseClass

class User(AbstractUser,MedicBaseClass):
    """
        Authentication Class
    """
    email = models.EmailField(
        'email_address',
        unique=True,
        error_messages={
            'unique' : 'Email ya ocupado con otro usuario.'
        }
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username', 'first_name','last_name']

    def __str__(self):
        return self.username

    def get_short_name(self):
        return self.username

    class Meta:
        db_table = "usuarios"