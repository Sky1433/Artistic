from django.urls import path
from . import views
app_name= "artistic"

urlpatterns=[
    path("home/", views.home, name="home"),
    path("gallery/", views.gallery,name="gallery"),
    path("details/", views.artDetails,name="details"),
    path("profile/",views.profile,name="profile"),
    path("edit/profile/",views.edit_profile,name="edit"),
    path("register/",views.register_user,name="register"),
    path("login/",views.login_user,name="login"),
    path("upload/",views.upload_artwork,name="upload"),
    path("modify/",views.modify_artwork,name="modify"),
    path("artists/",views.view_artists, name="artists"),
]