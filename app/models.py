from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True)
    mobile_no = PhoneNumberField(blank=False)
    profile_pic = models.ImageField(upload_to=user_path_directory, blank=True, null=True, default='media/default.jpg')
    date_updated = models.DateTimeField(auto_now=True)

    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]