from __future__ import unicode_literals

from django.db import models
from django.template.defaultfilters import slugify
from django.utils.text import slugify
from django.contrib.auth.models import User
from io import BytesIO
from django.core.files.uploadedfile import InMemoryUploadedFile
from django.core.files.base import ContentFile
from django.core.files import File
from django.utils import timezone
from django.conf import settings
from django.core.urlresolvers import reverse
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
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=128, blank=True)
    image = models.ImageField(upload_to='cottages', blank=True)
    likes = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True, related_name='cottage_likes')
    user = models.ForeignKey(settings.AUTH_USER_MODEL, default=1)
    region = models.ForeignKey(Region)
    address = models.CharField(max_length=128, blank=True)
    views = models.IntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Cottage, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("dog:show_cottage", args=[self.slug])

    def get_like_url(self):
        return reverse("dog:like-toggle", args=[self.slug])

    def get_api_like_url(self):
        return reverse("dog:api_like_cottage", args=[self.slug])



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
