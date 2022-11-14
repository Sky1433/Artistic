from django.shortcuts import render, redirect
from django.http import HttpRequest
from datetime import datetime
# Create your views here.
def home(request: HttpRequest):

    return render(request, "artistic/homePage.html")

def gallery(request: HttpRequest):

    return render(request, "artistic/galleryP.html")

def artDetails(request: HttpRequest):

    return render(request, "artistic/ArtDeatails.html")

def profile(request: HttpRequest):

    return render(request, "artistic/profilePage.html")
    
def register_user(request: HttpRequest):

    return render(request, "artistic/registerPage.html")
def login_user(request: HttpRequest):

    return render(request, "artistic/loginPage.html") 

def upload_artwork(request: HttpRequest):

    return render(request, "artistic/UploadPage.html")

def modify_artwork(request: HttpRequest):

    return render(request, "artistic/modifypost.html")