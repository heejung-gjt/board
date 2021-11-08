from django.db import models
import time


class TimeStampable(models.Model):
  created_at = models.DateTimeField(auto_now_add=True)
  updated_at = models.DateTimeField(auto_now=True)

  class Meta:
    abstract = True


class Deleteable(models.Model):
  deleted_at = models.BooleanField(default=False)

  class Meta:
    abstract = True

