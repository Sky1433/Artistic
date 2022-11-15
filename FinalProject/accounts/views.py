from django.shortcuts import render, redirect
from django.http import HttpRequest
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def register_user(request: HttpRequest):
    if request.method == "POST":

        new_user = User.objects.create_user(username=request.POST["username"], email= request.POST["email"], first_name=request.POST["first_name"], last_name=request.POST["last_name"], password=request.POST["password"])
        new_user.save()
    return render(request, "accounts/registerPage.html")
    
def login_user(request: HttpRequest):

    return render(request, "accounts/loginPage.html") 

    