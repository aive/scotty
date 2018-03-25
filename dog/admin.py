from django.contrib import admin
from dog.models import Cottage
from dog.models import UserProfile


class CottageAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}
class RegionAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('name',)}

class UserProfileAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug':('user',)}

#from dog.models import Cottage
admin.site.register(UserProfile)
admin.site.register(Cottage)
