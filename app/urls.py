from django.urls import path
from . import views


urlpatterns = [
    path('', views.SignUp, name='signup'),
    path('login', views.Login, name='login'),
    path('index', views.Index, name='index'),
    path('add_news', views.AddNews, name='add_news'),
]