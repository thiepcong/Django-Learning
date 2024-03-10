from django.db import models
from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser

# Create your models here.


class CustomUserManager (BaseUserManager):
    def create_user(self,email,password,**extra_field):
        email = self.normalize_email(email)

        user = self.model(
            email=email,
            **extra_field
        )

        user.set_password(password)

        user.save()

        return user

    def create_superuser(self,email,password,**extra_field):
        extra_field.setdefault("is_staff",True)
        extra_field.setdefault("is_superuser",True)

        if extra_field.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being true")
        
        if extra_field.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being true")
        
        return self.create_user(email=email,password=password,**extra_field)

class User(AbstractUser):
    email = models.CharField(max_length=80,unique=True)
    username = models.CharField(max_length=45)
    date_of_birth=models.DateField(null=True)

    objects=CustomUserManager()
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ['username']

    def __str__(self):
        return self.username

