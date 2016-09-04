from django.db import models


class ArticleCategory(models.Model):
    title = models.CharField(max_length=255)
    newspaper = models.ForeignKey('newspaper.Newspaper', null=True)
    description = models.TextField(max_length=10000)
    
    def __unicode__(self):
        return "{} ({})".format(self.title, self.newspaper)
        
    def __str__(self):
        return self.__unicode__()    
   
    
class Article(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    issue = models.ForeignKey('newspaper.Issue', null=True)
    category = models.ForeignKey('ArticleCategory', null=True)
    page = models.IntegerField(default=1)
    description = models.TextField(max_length=10000, null=True, blank=True)
    
    def __unicode__(self):
        return "{} ({}, {} - {})".format(self.title, self.issue, self.page, self.category.title)
        
    def __str__(self):
        return self.__unicode__()        