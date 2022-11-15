from django.shortcuts import render, redirect
from django.http import HttpRequest
from datetime import datetime
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from .models import Artwork,Comment
#from import accounts

# Create your views here.
def home(request: HttpRequest ):
    #if request.method == "POST":



    return render(request, "artistic/homePage.html")

def gallery(request: HttpRequest):
    ''' this function will view the artworks as a gallery'''

    return render(request, "artistic/galleryP.html")

def artDetails(request: HttpRequest):
    ''' this function will show the artwork details'''
    try:
        artwork = Artwork.objects.get(id=artwork_id)
        comments = Comment.objects.filter(artwork = artwork)
    except:
        return render(request , "artistic/home.html")

    return render(request, "artistic/ArtDeatails.html", {"artwork" : artwork, "comments" : comments})


    
def upload_artwork(request: HttpRequest):
    ''' this function let the artists who has premtion to upload thier artwork'''
    user : User = request.user

    if not (user.is_authenticated and user.has_perm("artistic.UploadPage")):
        return redirect("accounts:login")

    if request.method == "POST":
        new_artwork = Artwork(user = request.user, title=request.POST["title"], content = request.POST["content"], publish_date=request.POST["publish_date"], is_artist = request.POST["is_artist"], artwork_type=request.POST["artwork_type"] , image=request.FILES["image"])
        new_artwork.save()
    return render(request, "artistic/UploadPage.html", {"Artwork" : Artwork})

@login_required(login_url="/account/login/")

def modify_artwork(request: HttpRequest , artwork_id:int):

    ''' this function let the artists who has premtion to modify thier artwork'''
    try:
        artwork = Artwork.objects.get(id=artwork_id)
    except:
        return render(request , "artistic/not_found.html")

    if request.method == "POST":
        artwork.title = request.POST["title"]
        artwork.content = request.POST["content"]
        artwork.publish_date = request.POST["publish_date"]
        artwork.is_artist = request.POST["is_artist"]
        artwork.save()

        return redirect("artistic:gallery")

    artwork.publish_date = artwork.publish_date.isoformat("T", "hours").replace("+", ":")
    return render(request, "artistic/modifypost.html", {"artwork" : artwork})

def delete_artwork(request: HttpRequest, artwork_id:int):
    ''' this function will delete the artwork'''
    try:
        artwork = Artwork.objects.get(id=artwork_id)
    except:
        return render(request , "artistic/not_found.html")

    artwork.delete()

    return redirect("artistic:gallery")

def add_comment(request: HttpRequest, artwork_id:int):
    ''' this function will add comment the artwork'''
    artwork = Artwork.objects.get(id=artwork_id)

    if request.method == "POST":
        new_comment = Comment(artwork=artwork, name = request.POST["name"], content=request.POST["content"])
        new_comment.save()

    
    return redirect("artistic:artDetails", artwork_id)

def view_artwork(request: HttpRequest):
    ''' this function will list artwork and let them edit it or delete it '''
    
    if "search" in request.GET:
        artwork = Artwork.objects.filter(title__contains=request.GET["search"])
    else:
        artwork = Artwork.objects.all()
    return render(request, "artistic/viewArtwork.html", {"artwork" : artwork})


def view_artists(request: HttpRequest):
    ''' this function will view list of artist in the artist page'''

    return render(request, "artistic/viewartist.html")   


def profile(request: HttpRequest):
    ''' this function will preview the profile'''

    return render(request, "artistic/profilePage.html")
def edit_profile(request: HttpRequest):
    ''' this function will let the user edit thier profile'''

    return render(request, "artistic/editProfile.html")    