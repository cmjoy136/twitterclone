from django.shortcuts import render, HttpResponseRedirect, reverse
from django.contrib.auth.models import User
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet
from twitterclone.twitterusers.forms import TwitterUserForm

def create_user(request):
    html = 'createuser.html'
    form = TwitterUserForm()
    if request.method == 'POST':
        form = TwitterUserForm(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            user= User.objects.create_user(username=data['username'], password=data['password'])
            TwitterUser.objects.create(
                user=user,
                name= data['name'],
                bio= data['bio'],
            )
            return HttpResponseRedirect(reverse('homepage'))
    
    return render(request, html, {'form': form})

def twitter_user_profile(request, id):
    html = "tweeterprofile.html"
    twitteruser = TwitterUser.objects.filter(id=id).first()
    following = twitteruser.follow.count()
    tweet_count= Tweet.objects.filter(author=twitteruser).count()
    return render(request, html, {
        'data': twitteruser,
        'following':following,
        'tweet_count': tweet_count
        })

def follow_twitter_user(request, id):
    currentuser = request.user.twitteruser
    twitteruser = TwitterUser.objects.get(id=id)
    currentuser.follow.add(twitteruser)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

def unfollow_twitter_user(request, id):
    currentuser = request.user.twitteruser
    twitteruser = TwitterUser.objects.get(id=id)
    currentuser.follow.remove(twitteruser)
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
