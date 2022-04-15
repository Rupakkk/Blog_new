from datetime import datetime
from pickle import TRUE
from django.db import models
from django.forms import CharField
from django.contrib.auth.models import User
# from taggit.managers import TaggableManager


# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50)


class Blog(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    blog_title = models.CharField(max_length=50)
    description = models.TextField()
    view_count = models.PositiveIntegerField()
    datetime = models.DateTimeField(auto_now_add=True,null=True)
    
