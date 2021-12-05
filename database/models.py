from django.db import models

# Create your models here.


class Achievement(models.Model):
    username = models.CharField(max_length=100, default='')
    achievement = models.CharField(max_length=100, default='')