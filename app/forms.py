from django.forms import ModelForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from .models import User, News
from django import forms


class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'


class NewsForm(forms.ModelForm):
    class Meta:
        model = News
        fields = '__all__'