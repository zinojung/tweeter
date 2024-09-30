from django.db import models
from django.contrib.auth.models import AbstractUser



class User(AbstractUser):

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")

    first_name = models.CharField(
        max_length=150, editable=False
    )
    last_name = models.CharField(
        max_length=150, editable=False
    )
    name = models.CharField(
        max_length=150, default=""
    )