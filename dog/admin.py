from django.contrib import admin
from dog.models import Cottage
from dog.models import UserProfile


class CottageAdmin(admin.ModelAdmin):
    prepoulated_fields = {'slug':('name',)}

class UserProfileAdmin(admin.ModelAdmin):
    prepoulated_fields = {'slug':('user',)}

#from dog.models import Cottage
admin.site.register(UserProfile)
admin.site.register(Cottage)
