from django.db import models
from account.models import UserModel

class Post(models.Model):
    author = models.ForeignKey(UserModel, models.CASCADE, related_name='posts')
    title = models.CharField(max_length=200)
    accepted = models.BooleanField(default=False)
