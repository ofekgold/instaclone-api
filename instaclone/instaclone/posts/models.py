from django.db import models
from accounts.models import Account

# Create your models here.
class Post(models.Model):
    account = models.ForeignKey(Account, related_name='posts', on_delete='CASCADE')
    image = models.ImageField()
    description = models.CharField(blank=True, default='')

    def __str__(self):
        return self.description
