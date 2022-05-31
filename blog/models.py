from distutils.command.upload import upload
from django.core import validators
from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Post(models.Model):
    title = models.CharField(max_length=100)
    tekst = models.CharField(max_length=200)
    image=models.ImageField(upload_to="nohover",null=True)
    image=models.ImageField(upload_to="hover",null=True)
    slug = models.SlugField(unique=True, db_index=True)
    video = models.FileField( upload_to="videos", max_length=100)
    date = models.DateField(auto_now=True)
    

    def __str__(self):
        return self.title
        


