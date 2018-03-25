from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from dog import views
from .views import (
    CottageLikeToggle,
)


app_name = 'dog'
urlpatterns = [
    #Main
    url(r'^$', views.index, name='index'),
    #Region URLs
    url(r'^regions/$', views.regions, name='regions'),
    url(r'^add_region/$', views.add_region, name='add_region'),
    url(r'^region/(?P<region_name_slug>[\w\-]+)/$', views.show_region, name='show_region'),
    #Cottage URLs
    url(r'^region/(?P<region_name_slug>[\w\-]+)/add_cottage/$', views.add_cottage, name='add_cottage'),
    url(r'^cottage/(?P<cottage_name_slug>[\w\-]+)/$', views.show_cottage, name='show_cottage'),
    url(r'^cottage/(?P<cottage_name_slug>[\w\-]+)/like/$', CottageLikeToggle.as_view(), name='like-toggle'),
    url(r'^browse_cottages/$', views.browse_cottages, name='browse_cottages'),
    url(r'^mostviewed/$', views.mostviewed, name='mostviewed'),
    url(r'^mostliked/$', views.mostliked, name ='mostliked'),
    url(r'^cottage/(?P<cottage_name_slug>[\w\-]+)/review/$', views.review, name='review'),
    url(r'^cottage/(?P<cottage_name_slug>[\w\-]+)/sign/$', views.sign, name='sign'),
    url(r'^suggest_cottage/$', views.suggest_cottage, name='suggest_cottage'),
    ]
