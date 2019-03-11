from django.db import models
from accounts.models import Account
from posts.models import Post

# Create your models here.
class Like(models.Model):
    account = models.ForeignKey(Account, related_name='likes', on_delete='CASCADE')
    post = models.ForeignKey(Post, related_name='likes', on_delete='CASCADE')
    liked = models.BooleanField(default=False)
    
    def __str__(self):
        return self.liked
