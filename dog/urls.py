from django.conf.urls import url
from django.conf import settings
from django.conf.urls.static import static
from dog import views
from .views import (
    CottageLikeToggle,
    #CottageLikeAPIToggle,
)


app_name = 'dog'
urlpatterns = [
    url(r'^add_region/$', views.add_region, name='add_region'),
    url(r'^$', views.index, name='index'),
    url(r'^regions/$', views.regions, name='regions'),
    url(r'^searchresults/$', views.searchresults, name='searchresults'),
    url(r'^region/(?P<region_name_slug>[\w\-]+)/$', views.show_region, name='show_region'),
    url(r'^region/(?P<region_name_slug>[\w\-]+)/add_cottage/$', views.add_cottage, name='add_cottage'),
    url(r'^cottage/(?P<cottage_name_slug>[\w\-]+)/$', views.show_cottage, name='show_cottage'),
    url(r'^cottage/(?P<cottage_name_slug>[\w\-]+)/like/$', CottageLikeToggle.as_view(), name='like-toggle'),
    #url(r'^api/(?P<cottage_name_slug>[\w-]+)/like/$', CottageLikeAPIToggle.as_view(), name='like-api-toggle'),
    url(r'^cottage/(?P<cottage_name_slug>[\w\-]+)/review/$', views.review, name='review'),
    url(r'^cottage/(?P<cottage_name_slug>[\w\-]+)/sign/$', views.sign, name='sign'),
    url(r'^restricted/', views.restricted, name='restricted'),
    ] 
