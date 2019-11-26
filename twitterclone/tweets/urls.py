from django.contrib import admin
from django.urls import path
from twitterclone.tweets import views, models


urlpatterns = [
    path('addtweet/', views.add_tweet_view, name='addtweet'),
    path('liketweet/<int:id>/', views.like_tweet_view, name='liketweet'),
]