from django.db import models
from behaviors import Deleteable, TimeStampable
from user.models import User


class Post(TimeStampable):
  title = models.CharField(max_length=124)
  content = models.TextField()
  writer = models.ForeignKey(User, on_delete=models.CASCADE, related_name='article')
