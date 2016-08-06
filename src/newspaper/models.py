from django.db import models

class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    
    def __unicode__(self):
        return self.title
    
    def get_absolute_url(self):
        return "/newspaper/%i/" % self.id