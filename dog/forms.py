from django import forms
from dog.models import Cottage
from dog.models import Region
from dog.models import UserProfile
from django.contrib.auth.models import User 

class RegionForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the region name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Region
        fields = ('name',)

class CottageForm(forms.ModelForm):
    title = forms.CharField(max_length=128, help_text="Please enter the name of the cottage.")
    address = forms.CharField(max_length=200, help_text="Please enter the address of the cottage.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    class Meta:
        model = Cottage
        exclude = ('region',)

    def clean(self):
        cleaned_data = self.cleaned_data
        url = cleaned_data.get('url')

        if url and not url.startswith('http://'):
            url = 'http://' + url
            cleaned_data['url'] = url

            return cleaned_data

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture')

