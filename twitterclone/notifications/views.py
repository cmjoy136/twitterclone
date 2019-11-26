from django.shortcuts import render, HttpResponseRedirect, reverse
from twitterclone.notifications.models import Notification

def notification_view(request):
    html = 'notifications.html'
    notifications = Notification.objects.filter(notify=request.user.twitteruser)
    for notification in notifications:
        notification.delete()
    return render(request, html, {'notifications': notifications})