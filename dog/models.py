from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.core.files import File
from django.utils import timezone
import os

class Region(models.Model):
    name = models.CharField(max_length=128, unique=True)
    views = models.IntegerField(default=0)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Region, self).save(*args, **kwargs)

    def __str__(self):
        return self.name


class Cottage(models.Model):
    region = models.ForeignKey(Region)
    name = models.CharField(max_length=128)
    image = models.ImageField(upload_to='cottages', blank=True)
    address = models.CharField(max_length=128, blank=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)
    

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cottage, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

class Comment(models.Model):
    name = models.CharField(max_length=20, blank=True)
    comment = models.TextField(blank=True)
    date_added = models.DateTimeField(default=timezone.now)
    cottage = models.ForeignKey(Cottage, related_name='comments',blank=True, null=True)

    def __str__(self):
        return self.name
      
       
    '''@property
    def image_url(self):
        if self.image and hasattr(self.image, 'url'):
            return self.image.url
'''


class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

def __str__(self):
        return self.user.username
