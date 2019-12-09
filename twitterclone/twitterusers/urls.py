from django.contrib import admin
from django.urls import path
from twitterclone.twitterusers import views

urlpatterns = [
    path('createuser/', views.CreateUser.as_view(), name='createuser'),
    path('twitteruser/<int:id>/', views.TwitterUserProfile.as_view(), name='tweeterprofile'),
    path('follow/<int:id>/', views.FollowTwitterUser.as_view(), name='followtweeter'),
    path('unfollow/<int:id>/', views.UnfollowTwitterUser.as_view(), name='unfollow'),
]