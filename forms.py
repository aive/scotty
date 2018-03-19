from django import forms
from dog.models import Comment
from dog.models import Cottage
from dog.models import Region
from dog.models import UserProfile
from django.contrib.auth.models import User
from django.utils.safestring import mark_safe



class CommentForm (forms.Form):
    name = forms.CharField(max_length=20, widget=forms.TextInput(attrs={'class' : 'form-control', 'placeholder':'Name'}))
    comment = forms.CharField (widget=forms.Textarea(attrs={'class' : 'form-control' ,'placeholder' : 'Comment'}))
    date_added = forms.DateTimeField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Comment
        exclude = ('cottage',)

class RegionForm(forms.ModelForm):
    name = forms.CharField(max_length=128, help_text="Please enter the region name.")
    views = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    likes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Region
        fields = ('name',)

class CottageForm(forms.ModelForm):
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    class Meta:
        model = Cottage
        fields = ('name', 'image', 'address')
        exclude = ('region','user', 'likes', 'views')

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
