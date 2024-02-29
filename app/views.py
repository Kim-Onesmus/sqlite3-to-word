from django.shortcuts import render, redirect
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import auth, User
from django.contrib import messages
from .models import User
from .forms import UserForm

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


def Index(request):
    return render(request, 'app/index.html')


def AddNews(request):
    pass


def Profile(request):
    user = request.user
    form = UserForm(instance=user)
    password_form = PasswordChangeForm(request.user)
    if request.method == 'POST':
        form = UserForm(request.POST, request.FILES, instance=client)
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