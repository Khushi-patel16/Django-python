from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField


# Create your models here.
class News(models.Model):
   title = models.CharField(max_length=100)
   description = models.TextField()
   slug = AutoSlugField(populate_from ='title', unique=True,null = True,default=None)

   def __str__(self):
       return self.title
   

