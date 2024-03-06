from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import User, News
from .forms import UserForm, NewsForm
import pandas as pd
from django.http import HttpResponse
from django.shortcuts import render
import sqlite3
from django.http import HttpResponse
from django.shortcuts import render
from django.db import connection
from .utils import export_to_word, export_to_csv, export_to_excel, export_to_json

# Create your views here.

def SignUp(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        mobile_no = request.POST['mobile_no']
        password = request.POST['password']
        password1 = request.POST['password1']

        if password==password1:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email taken')
                return redirect('signup')

            elif User.objects.filter(mobile_no=mobile_no).exists():
                messages.error(request, 'Phone number taken')
                return redirect('signup')

            else:
                user_details = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=email, mobile_no=mobile_no, password=password)
                user_details.save()
                messages.info(request, 'Account created')
                return redirect('login')
        else:
            messages.error(request, 'Password dont match')
            return redirect('login')
    else:
        return render(request, 'app/account/register.html')
    return render(request, 'app/account/register.html')


def Login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            messages.info(request, 'Welcome back')
            return redirect('index')
        else:
            messages.error(request, 'Invalid credetials')
            return redirect('login')
        
    else:
        return render(request, 'app/account/login.html')
    return render(request, 'app/account/login.html')


# def get_all_table_names():
#     with connection.cursor() as cursor:
#         cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
#         tables = [table[0] for table in cursor.fetchall()]
#     return tables


# def get_table_columns(table_name):
#     with connection.cursor() as cursor:
#         cursor.execute(f"PRAGMA table_info({table_name})")
#         columns = [column[1] for column in cursor.fetchall()]
#         print(f"Columns for {table_name}: {columns}")
#     return columns



def Index(request):
    return render(request, 'app/index.html')


def get_all_table_names():
    with connection.cursor() as cursor:
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        tables = [table[0] for table in cursor.fetchall()]
    return tables


from django.http import JsonResponse
def get_table_columns(request):
    selected_table = request.GET.get('selected_table', '')
    columns = get_table_columns(selected_table)
    return JsonResponse({'columns': columns})


def export_word(request):
    tables = get_all_table_names()
    selected_table = request.POST.get('selected_table', '')
    table_columns = get_table_columns(selected_table) if selected_table else []

    if request.method == 'POST':
        selected_columns = request.POST.getlist('selected_columns')

        print(f"Selected Table: {selected_table}")
        print(f"Selected Columns: {selected_columns}")

        if selected_table:
            db_name = "db.sqlite3"  # Update with the correct path

            # If no columns are selected, export all columns
            if not any(selected_columns):
                selected_columns = get_table_columns(selected_table)
                print(f"Columns after get_table_columns: {selected_columns}")
            else:
                selected_columns = list(set(selected_columns))  # Ensure unique columns

            output_filename = f"{selected_table}_data.docx"

            # Your export_to_word function implementation goes here
            export_to_word(db_name, selected_table, output_filename, selected_columns)

            # Provide the file for download
            with open(output_filename, 'rb') as docx_file:
                response = HttpResponse(docx_file.read(), content_type="application/vnd.openxmlformats-officedocument.wordprocessingml.document")
                response['Content-Disposition'] = f'attachment; filename={output_filename}'
                return response

    # Render the template with a form to choose the table and columns
    return render(request, 'app/export/export_word.html', {'tables': tables, 'table_columns': table_columns})

def exportExcel(request):
    tables = get_all_table_names()
    selected_table = request.POST.get('selected_table', '')
    table_columns = get_table_columns(selected_table) if selected_table else []

    if request.method == 'POST':
        selected_columns = request.POST.getlist('selected_columns')

        print(f"Selected Table: {selected_table}")
        print(f"Selected Columns: {selected_columns}")

        if selected_table:
            db_name = "db.sqlite3"  # Update with the correct path

            # If no columns are selected, export all columns
            if not any(selected_columns):
                selected_columns = get_table_columns(selected_table)
                print(f"Columns after get_table_columns: {selected_columns}")
            else:
                selected_columns = list(set(selected_columns))  # Ensure unique columns

            output_filename = f"{selected_table}_data.xlsx"

            # Your export_to_word function implementation goes here
            export_to_excel(db_name, selected_table, output_filename, selected_columns)

            # Provide the file for download
            with open(output_filename, 'rb') as docx_file:
                response = HttpResponse(docx_file.read(), content_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet")
                response['Content-Disposition'] = f'attachment; filename={output_filename}'
                return response

    # Render the template with a form to choose the table and columns
    return render(request, 'app/export/export_excel.html', {'tables': tables, 'table_columns': table_columns})


def exportCsv(request):
    tables = get_all_table_names()
    selected_table = request.POST.get('selected_table', '')
    table_columns = get_table_columns(selected_table) if selected_table else []

    if request.method == 'POST':
        selected_columns = request.POST.getlist('selected_columns')

        print(f"Selected Table: {selected_table}")
        print(f"Selected Columns: {selected_columns}")

        if selected_table:
            db_name = "db.sqlite3"  # Update with the correct path

            # If no columns are selected, export all columns
            if not any(selected_columns):
                selected_columns = get_table_columns(selected_table)
                print(f"Columns after get_table_columns: {selected_columns}")
            else:
                selected_columns = list(set(selected_columns))  # Ensure unique columns

            output_filename = f"{selected_table}_data.csv"

            # Your export_to_word function implementation goes here
            export_to_csv(db_name, selected_table, output_filename, selected_columns)

            # Provide the file for download
            with open(output_filename, 'rb') as docx_file:
                response = HttpResponse(docx_file.read(), content_type="text/csv")
                response['Content-Disposition'] = f'attachment; filename={output_filename}'
                return response

    # Render the template with a form to choose the table and columns
    return render(request, 'app/export/export_csv.html', {'tables': tables, 'table_columns': table_columns})



def exportJson(request):
    tables = get_all_table_names()
    selected_table = request.POST.get('selected_table', '')
    table_columns = get_table_columns(selected_table) if selected_table else []

    if request.method == 'POST':
        selected_columns = request.POST.getlist('selected_columns')

        print(f"Selected Table: {selected_table}")
        print(f"Selected Columns: {selected_columns}")

        if selected_table:
            db_name = "db.sqlite3"  # Update with the correct path

            # If no columns are selected, export all columns
            if not any(selected_columns):
                selected_columns = get_table_columns(selected_table)
                print(f"Columns after get_table_columns: {selected_columns}")
            else:
                selected_columns = list(set(selected_columns))  # Ensure unique columns

            output_filename = f"{selected_table}_data.json"

            # Your export_to_word function implementation goes here
            export_to_json(db_name, selected_table, output_filename, selected_columns)

            # Provide the file for download
            with open(output_filename, 'rb') as docx_file:
                response = HttpResponse(docx_file.read(), content_type="application/json")
                response['Content-Disposition'] = f'attachment; filename={output_filename}'
                return response

    # Render the template with a form to choose the table and columns
    return render(request, 'app/export/export_json.html', {'tables': tables, 'table_columns': table_columns})
    



def AddNews(request):
    if request.method == 'POST':
        form = NewsForm(request.POST, request.FILES)
        if form.is_valid():
            news_instance = form.save(commit=False)
            news_instance.user = request.user
            news_instance.save()
            messages.info(request, 'News uploaded')
            return redirect('all_news')
    else:
        form = NewsForm()

    context = {'form': form}
    return render(request, 'app/add_news.html', context)


def AllNews(request):
    all_news = News.objects.all()

    context = {'all':all_news}
    return render(request, 'app/all_news.html', context)

def Profile(request):
    user = request.user
    print(user)
    form = UserForm(instance=user)
    password_form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=user)
        password_form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Profile edited')
            return redirect('profile')

        if password_form.is_valid():
            password_form.save()
            messages.info(request, 'Profile information updated')
            return redirect('login')
    
    context = {'form':form, 'password_form':password_form}
    return render(request, 'app/account/profile.html', context)


def Logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.info(request, 'Logged Out')
        return redirect('login')
    return render(request, 'app/account/logout.html')