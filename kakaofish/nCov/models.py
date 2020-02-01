from django.db import models

class News(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=1000)
    description = models.CharField(max_length=1000)
    pubDate = models.CharField(max_length=50)
