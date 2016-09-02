from django.db import models

class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.__unicode__()

    def get_absolute_url(self):
        return "/newspaper/%i/" % self.id
    

class Year(models.Model):
    year = models.IntegerField()
    
    def __unicode__(self):
        return self.year.__str__()
    
    def __str__(self):
        return self.__unicode__()


    def get_absolute_url(self):
        return "/newspaper/year/%i/" % self.year
    
    
class Issue(models.Model):
    year = models.ForeignKey(Year)
    newspaper = models.ForeignKey(Newspaper)
    issue = models.IntegerField(default=0)
    description = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return "{} {}'{} {}".format(self.newspaper, self.issue, self.year, self.description)
        
    def __str__(self):
        return self.__unicode__()