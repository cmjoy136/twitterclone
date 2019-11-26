from django import forms
from twitterclone.tweets.models import Tweet

class AddTweet(forms.ModelForm):
    class Meta:
        model = Tweet
        fields = ['tweet_content']