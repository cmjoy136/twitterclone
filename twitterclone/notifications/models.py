from django.db import models
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet

class Notification(models.Model):
    notify = models.ForeignKey(TwitterUser, on_delete=models.CASCADE)
    seen = models.BooleanField(default=False)
    tweet_notif = models.ForeignKey(Tweet, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.notify} - {self.tweet_notif}'