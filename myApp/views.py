from cgitb import text
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature


# Create your views here.
def index(request):
    features = Feature.objects.all()
    return render(request, 'index.html', {'features': features})

def register(request):
    if request.method == 'POST':
        # if the request method is a post, the user must have completed the form
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']
        # the values for username, email, password and password2 are collected

        if password == password2:
            # Checks if password is the same as password2 to prevent any user errors
            if User.objects.filter(email=email).exists():
                # Checks if there is a user object with the same email if there is, it gives an error message and redirects back to the register page
                messages.info(request, 'Email has already been used')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                # Checks if there is a user object with the same username
                messages.info(request, 'Username has already been used')
                # Provides an error message
                return redirect('register')
                # Redirects back to the register page
            else:
                user = User.objects.create_user(username=username, email=email, password=password)
                # Creates a user object with the email, username and password provided
                user.save();
                # Saves the user
                return redirect('login')
                # Redirects to the login page
        else:
            messages.info(request, 'Passwords do not match')
            # If the passwords do not match, there is an error message
            return redirect('register')
            # The user is redirected back to the register page
    else:
        return render(request, 'register.html')
        # If the request is not a POST, it just renders the register page

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')