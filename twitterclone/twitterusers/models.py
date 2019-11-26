from django.db import models
from django.contrib.auth.models import User

class TwitterUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    bio = models.TextField(blank=True, null=True)
    follow = models.ManyToManyField('self', symmetrical=False, blank=True, related_name='who_you_follow')

    def __str__(self):
        return self.name
    
     