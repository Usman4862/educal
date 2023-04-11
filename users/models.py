from django.db import models
from django.contrib.auth.models import AbstractUser
from .managers import CustomUserManager


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = "M", ("Male"),
        FEMALE = "FM", ("Female"),
        OTHERS = "O" , ("Others"),
    email = models.EmailField("email address", unique=True, blank=False, null=False)
    photo = models.ImageField(upload_to="static/images")
    gender = models.CharField(max_length=15, null=True, blank=False, choices=GenderChoices.choices)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.CharField(max_length=300, null=True, blank=True)
    contact = models.PositiveIntegerField(default=00000000000)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["gender"]

    objects = CustomUserManager()

    def __str__(self) -> str:
        return self.email