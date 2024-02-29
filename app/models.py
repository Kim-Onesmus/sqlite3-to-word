from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import AbstractUser
from django.db import models

category_choice = [
    ('sports','sports'),
    ('education','education'),
    ('politics','politics'),
    ('administrative','administrative'),
    ('religious','religious'),
]

class User(AbstractUser):
    first_name = models.CharField(max_length=50, blank=False)
    last_name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(unique=True)
    mobile_no = PhoneNumberField(blank=False)
    profile_pic = models.ImageField(upload_to='media', blank=True, null=True, default='media/default.jpg')
    date_updated = models.DateTimeField(auto_now=True)

    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username"]


class News(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=200, choices=category_choice)
    tittle = models.CharField(max_length=300)
    image = models.ImageField(upload_to='media')
    text = models.TextField(max_length=1000)
    created_date = models.DateField(auto_now_add=True)
    created_time = models.TimeField(auto_now_add=True)
