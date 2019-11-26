from django.shortcuts import render, HttpResponseRedirect, reverse
from twitterclone.tweets.models import Tweet
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.forms import AddTweet
from twitterclone.notifications.models import Notification
import re

def add_tweet_view(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    html = 'addtweet.html'
    form =AddTweet()

    if request.method == 'POST':
        form = AddTweet(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            tweet= Tweet.objects.create(
                author=request.user.twitteruser,
                tweet_content= data['tweet_content']
            )
            if '@' in data['tweet_content']:
                handles= re.findall(r'@(\w+)', data['tweet_content'])
                for handle in handles:
                    matched_user= TwitterUser.objects.filter(user__username=handle).first()
                    Notification.objects.create(
                        notify= matched_user,
                        tweet_notif=tweet,
                    )
            return HttpResponseRedirect(reverse('homepage'))

    return render(request, html, {'tweetform': form})

def like_tweet_view(request, id):
    tweet = Tweet.objects.get(id=id)
    if tweet.like == 0:
        tweet.like += 1
        tweet.save()
    else:
        tweet.like -= 1
        tweet.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))