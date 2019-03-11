from django.db import models
from accounts.models import Account
from posts.models import Post

# Create your models here.
class Comment(models.Model):
    account = models.ForeignKey(Account, related_name='comments', on_delete='CASCADE')
    post = models.ForeignKey(Post, related_name='comments', on_delete='CASCADE')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.text