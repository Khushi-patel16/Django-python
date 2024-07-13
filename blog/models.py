from django.db import models
from tinymce.models import HTMLField
from autoslug import AutoSlugField



# Create your models here.
class Subscribe(models.Model):
    email = models.EmailField()

    def __str__(self):
        return self.email
    

class ContactModel(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    subject = models.CharField(max_length=200)
    message = models.TextField()

    def __str__(self):
        return self.name
    
# from django.db import models
# from django.utils.text import slugify

# class Service(models.Model):
    # service = models.CharField(max_length=200)
    # description = models.TextField()
    # icon = models.CharField(max_length=100)
    # slug = models.SlugField(unique=True, blank=True)
# 
    # def save(self, *args, **kwargs):
        # if not self.slug:
            # self.slug = slugify(self.service)
        # super(Service, self).save(*args, **kwargs)

class ServiceModel(models.Model):
    icon = models.CharField(max_length=100)
    service = models.CharField(max_length=50)
    icon_desc = models.CharField(max_length=100,default='')
    slug = AutoSlugField(populate_from ='service', unique=True,null = True,default=None)

    def __str__(self):
        return self.service
    
class ServiceItem(models.Model):
    service = models.ForeignKey(ServiceModel, related_name='service_items', on_delete=models.CASCADE)
    description = models.TextField()

    def __str__(self):
        return self.description[:50]

class AboutModel(models.Model):
    
    image = models.ImageField(upload_to='img/',max_length=100) 
    tagline = models.TextField() 
    para1 = models.TextField()
    #icon = models.CharField(max_length=50)
    #icon_des = models.TextField()
    para2 = models.TextField(default='default_value')

    def __str__(self):
        return self.tagline
    
class ListItem(models.Model):
    about = models.ForeignKey(AboutModel, related_name='list_items', on_delete=models.CASCADE)
    icon = models.CharField(max_length=50)
    icon_des = models.CharField(max_length=250)

    def __str__(self):
        return self.icon_des[:50]
     
class ClientModel(models.Model):
    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='client/', max_length=100)

    def __str__(self):
        return self.title
    
class Counts(models.Model):
    icon = models.CharField(max_length=50)
    counter_end = models.IntegerField()
    title = models.CharField(max_length=50)
    description  = models.TextField()

    def __str__(self):
        return self.title

class Testimonials(models.Model):
    image = models.ImageField(upload_to='testi/', max_length=100)
    name = models.CharField(max_length=50)  
    post = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.name
    

class Team(models.Model):
    image = models.ImageField(upload_to='team/', max_length=100)
    name = models.CharField(max_length=50)
    post = models.CharField(max_length=50)

    def __str__(self):
        return self.name
    
class Features(models.Model):
    icon = models.CharField(max_length=100)
    title = models.CharField(max_length=50)
    description = models.TextField()

    def __str__(self):
        return self.title    

class Portfolio(models.Model):
    CATEGORY_CHOICES = [
        ('app', 'App'),
        ('card', 'Card'),
        ('web', 'Web'),
    ]
    title = models.CharField(max_length=100)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES)
    image = models.ImageField(upload_to='portfolio/', max_length=100)

    def __str__(self):
        return self.title
    
class Portfolio_details(models.Model):
    title = models.CharField(max_length=200)
    category = models.CharField(max_length=100)
    client = models.CharField(max_length=100)
    project_date = models.DateField()
    project_url = models.URLField()
    tagline = models.TextField(default='')
    description = models.TextField()
    #images = models.JSONField(default= dict)  # Storing image URLs as JSON list

    def __str__(self):
        return self.title


class PortfolioImage(models.Model):
    portfolio = models.ForeignKey(Portfolio_details, related_name='portfolio_images', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='portfolio_images/')

    def __str__(self):
        return self.image.url
    

class Header(models.Model):
    site_name = models.CharField(max_length=50)
    line1 = models.CharField(max_length=150)
    line2 = models.CharField(max_length=150)

    def __str__(self):
        return self.site_name
    
class Hero(models.Model):
    icon = models.CharField(max_length=50)
    title = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title

class Footer(models.Model):
    address = models.CharField(max_length=200)
    phone = models.CharField(max_length=10)
    email = models.EmailField()
    newsletter =  models.CharField(max_length=200)

    def __str__(self):
        return self.address
    
class Social(models.Model):
    icon = models.CharField(max_length=100)
    link = models.CharField(max_length=300, default= '#')

    def __str__(self):
        return self.icon
    
      