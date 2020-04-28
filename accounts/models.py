from django.contrib.auth.models import AbstractUser
from django.db import models

from backend.utils import get_upload_path
from cvhus.models import Cvhu


class Account(AbstractUser):
    cvhu = models.ForeignKey(Cvhu, on_delete=models.SET_NULL, null=True, default=None)
    phone = models.CharField(max_length=10, unique=True, null=True, blank=True)
    image = models.ImageField(default="avatar.png", upload_to=get_upload_path, blank=True)

    def __str__(self):
        return "{0} - {1}".format(self.username, self.get_full_name())

    def get_full_name(self):
        return "{0} {1}".format(self.first_name, self.last_name)

    def get_short_name(self):
        return self.first_name

