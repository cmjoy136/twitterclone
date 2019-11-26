from django.db import models
from django.contrib.auth.models import User
from twitterclone.twitterusers.models import TwitterUser

class Tweet(models.Model):
    author = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    tweet_content = models.CharField(max_length=140)
    datetime = models.DateTimeField(auto_now_add=True)
    like = models.IntegerField(default=0)

    def __str__(self):
        return self.tweet_content
