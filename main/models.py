from django.db import models


# Create your models here.
class short_urls(models.Model):
    short_url = models.CharField(max_length=50)
    long_url = models.URLField(max_length=200)
    link = models.CharField(max_length=100000000000)
    
    def __str__(self):
        return self.short_url
    