from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User

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
    title = models.CharField(max_length=128)
    address = models.CharField(max_length=128, blank=True)
    views = models.IntegerField(default=0)

    def __str__(self):
        return self.title

class UserProfile(models.Model):
    user = models.OneToOneField(User)
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

def __str__(self):
        return self.user.username
