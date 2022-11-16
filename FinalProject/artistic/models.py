from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Artwork(models.Model):
    #fill types the same as the navbar in the gallrey page

    artwork_type_choices = models.TextChoices("Artwork Type", ["Painting", "Digital", "Crafts"])
    
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=1024)
    content = models.TextField()
    publish_date = models.DateTimeField()
    image = models.ImageField(upload_to="images/")
    is_artist = models.BooleanField(null=True)
    artwork_type  = models.CharField(max_length=64, choices = artwork_type_choices.choices, default=artwork_type_choices.Painting)

    def __str__(self) -> str:
        return f"{self.title}, {self.publish_date}"


class Comment(models.Model):

    artwork = models.ForeignKey(Artwork, on_delete = models.CASCADE)
    name = models.CharField(max_length=256)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now=True)



    def __str__(self):
        return f"{self.name}, {self.content}"
