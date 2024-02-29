from django.contrib import admin
from .models import User

# Register your models here.
@admin.register(User)
class UserTable(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'mobile_no', 'date_updated', 'profile_pic')