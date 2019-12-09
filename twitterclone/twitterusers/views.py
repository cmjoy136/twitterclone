from django.shortcuts import render, HttpResponseRedirect, reverse
from django.views import View
from django.contrib.auth.models import User
from twitterclone.twitterusers.models import TwitterUser
from twitterclone.tweets.models import Tweet
from twitterclone.twitterusers.forms import TwitterUserForm

class CreateUser(View):
    html = 'createuser.html'
    form = TwitterUserForm()

    def get(self, request, *args, **kwargs):
        form = TwitterUserForm()
        return render(request, self.html, {'form': form})

    def post(self, request, *args, **kwargs):
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
        return render(request, self.html, {'form': form})

class TwitterUserProfile(View):
    html = "tweeterprofile.html"
    def get(self, request, id, *args, **kwargs):
        twitteruser= TwitterUser.objects.filter(id=id).first()
        following = twitteruser.follow.count()
        tweet_count = Tweet.objects.filter(author=twitteruser).count()
        return render(request, self.html, {
            'data': twitteruser,
            'following':following,
            'tweet_count': tweet_count
            })


class FollowTwitterUser(View):
    def get(self, request, id, *args, **kwargs):
        currentuser = request.user.twitteruser
        twitteruser = TwitterUser.objects.get(id=id)
        currentuser.follow.add(twitteruser)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

class UnfollowTwitterUser(View):
    def get(self, request, id, *args, **kwargs):
        currentuser = request.user.twitteruser
        twitteruser = TwitterUser.objects.get(id=id)
        currentuser.follow.remove(twitteruser)
        return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))