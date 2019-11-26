from django.contrib import admin
from django.urls import path
from twitterclone.notifications import views

urlpatterns = [
    path('notifications/', views.notification_view, name='notificationpage')
]