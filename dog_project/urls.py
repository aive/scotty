from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from dog import views


urlpatterns = [
    
    # INDEX [HOME]
    url(r'^$', views.index, name='index'),
    
    # INCLUDE DOG APP URLS
    # [We have kept all of the urls in the app]
    url(r'^dog/', include('dog.urls')),

    
    
    # ADMIN SITE
    url(r'^admin/', admin.site.urls),
    # REGISTRATION
    url(r'^accounts/', include('registration.backends.simple.urls')),
    url(r'^accounts/register/$', views.MyRegistrationView, name='registration_register'),
    ]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()
