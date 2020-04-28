from django.core.exceptions import ValidationError
from django.db import models
from django_countries.fields import CountryField

from backend.utils import get_upload_cvhu_logo


def codepost_validator(instance):

    if len(instance) != 5 :
        raise ValidationError("Erreur Format de Code Postal")


class Cvhu(models.Model):

    name = models.CharField(max_length=50, default="")
    siret = models.CharField(max_length=20, default="", unique=True)
    vatnumber = models.CharField(max_length=20, default="", unique=True)
    agrnumber = models.CharField(max_length=10, default="", unique=True)
    address = models.CharField(max_length=100, default="", blank=True)
    address2 = models.CharField(max_length=100, default="", blank=True)
    postcode = models.PositiveSmallIntegerField(blank=True, validators=[codepost_validator])
    city = models.CharField(max_length=20, default="", blank=True)
    country = CountryField()
    tel = models.CharField(max_length=10, default="",blank=True)
    email = models.EmailField(blank=True)
    logoimage = models.ImageField(upload_to=get_upload_cvhu_logo)

    def get_current_users(self):
        return self.account_set()

    def __str__(self):
        return "{0} - {1}".format(self.name, self.agrnumber)