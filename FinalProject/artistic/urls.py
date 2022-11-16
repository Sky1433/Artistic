from django.urls import path
from . import views

app_name= "artistic"
#<artwork_id>/ for modify and upload and delete
urlpatterns=[
    path("home/", views.home, name="home"),
    path("gallery/", views.gallery,name="gallery"),
    path("details/", views.artDetails,name="details"),
    path("profile/",views.profile,name="profile"),
    path("edit/profile/",views.edit_profile,name="edit"),
    path("view/profile/",views.follow_user,name="view"),
    path("upload/",views.upload_artwork,name="upload"),
    path("myArtwork/",views.view_artwork,name="myArtwork"),
    path("delete/<artwork_id>/",views.delete_artwork,name="delete"),
    path("artists/",views.view_artists, name="artists"),
    path("artwork/<artwork_id>/comment/new/", views.add_comment, name="add_comment"), 
]