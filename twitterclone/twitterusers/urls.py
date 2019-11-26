from django.contrib import admin
from django.urls import path
from twitterclone.twitterusers import views

urlpatterns = [
    path('createuser/', views.create_user, name='createuser'),
    path('twitteruser/<int:id>/', views.twitter_user_profile, name='tweeterprofile'),
    path('follow/<int:id>/', views.follow_twitter_user, name='followtweeter'),
    path('unfollow/<int:id>/', views.unfollow_twitter_user, name='unfollow'),
]