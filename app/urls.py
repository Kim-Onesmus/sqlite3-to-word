from django.urls import path
from . import views


urlpatterns = [
    path('', views.SignUp, name='signup'),
    path('login', views.Login, name='login'),
    path('index', views.Index, name='index'),
    path('get_table_columns', views.get_table_columns, name='get_table_columns'),
    path('export_word', views.export_word, name='export_word'),
    path('export_excel', views.exportExcel, name='export_excel'),
    path('export_csv', views.exportCsv, name='export_csv'),
    path('export_json', views.exportJson, name='export_json'),
    path('add_news', views.AddNews, name='add_news'),
    path('all_news', views.AllNews, name='all_news'),
    path('profile', views.Profile, name='profile'),
    path('logout', views.Logout, name='logout'),
]