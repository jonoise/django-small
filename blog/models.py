from django.db import models
from account.models import UserModel

class Post(models.Model):
    author = models.ForeignKey(UserModel, models.CASCADE, related_name='posts')

