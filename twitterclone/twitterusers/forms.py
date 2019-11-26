from django import forms
from django.contrib.auth.models import User
from twitterclone.twitterusers.models import TwitterUser
from django.forms import widgets


class TwitterUserForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea)
    username = forms.CharField(max_length=50)
    password = forms.CharField(widget=forms.PasswordInput)