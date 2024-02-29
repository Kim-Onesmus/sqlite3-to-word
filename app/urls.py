from django.urls import path
from . import views


urlpatterns = [
    path('', views.SignUp, name='signup'),
    path('login', views.Login, name='login'),
    path('index', views.Index, name='index'),
    path('export_word', views.export_word, name='export_word'),
    path('add_news', views.AddNews, name='add_news'),
    path('all_news', views.AllNews, name='all_news'),
    path('profile', views.Profile, name='profile'),
    path('logout', views.Logout, name='logout'),
]