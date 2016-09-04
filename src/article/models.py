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
    title = models.CharField(max_length=255)
    issue = models.ForeignKey('newspaper.Issue', null=True)
    category = models.ForeignKey('ArticleCategory', null=True)
    description = models.TextField(max_length=10000)
    
    def __unicode__(self):
        return "{} ({} - {})".format(self.title, self.issue, self.category.title)
        
    def __str__(self):
        return self.__unicode__()        