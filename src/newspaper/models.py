from django.db import models

    
class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    # issues = models.ManyToManyField('Issue')
    
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.__unicode__()

    def get_absolute_url(self):
        return "/newspaper/{}/".format(self.id)
    
    def get_years(self):
        return self.issue_set.all()
    

class Year(models.Model):
    year = models.IntegerField()
    # issues = models.ManyToManyField('Issue')
    
    def __unicode__(self):
        return self.year.__str__()
    
    def __str__(self):
        return self.__unicode__()

    
class Issue(models.Model):
    newspaper = models.ForeignKey('Newspaper', null=True)
    year = models.ForeignKey('Year', null=True)
    issue = models.IntegerField(default=0)
    description = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return "{} {}'{} {}".format(self.newspaper, self.issue, self.year, self.description)
        
    def __str__(self):
        return self.__unicode__()
    
    def get_absolute_url(self):
        return "/newspaper/{}/{}/{}".format(self.newspaper.id, self.year.year, self.issue)