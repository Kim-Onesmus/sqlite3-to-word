from django.contrib import admin
from .models import User, News

# Register your models here.
@admin.register(User)
class UserTable(admin.ModelAdmin):
    list_display = ('email', 'first_name', 'last_name', 'mobile_no', 'date_updated', 'profile_pic')


@admin.register(News)
class NewsTable(admin.ModelAdmin):
    list_display = ('user', 'category', 'tittle', 'image', 'text', )