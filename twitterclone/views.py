from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.decorators import login_required
from twitterclone.tweets.models import Tweet
from twitterclone.twitterusers.models import TwitterUser

def index(request):
    if not request.user.is_authenticated:
        return HttpResponseRedirect(reverse('login'))
    html = 'index.html'
    tweets = Tweet.objects.all().order_by('-datetime')

    return render(request, html, {'tweets': tweets})