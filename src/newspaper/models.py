from django.db import models
from django.core.urlresolvers import reverse

    
class Newspaper(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000, blank=True)
    slug = models.SlugField(unique=True)
    # issues = models.ManyToManyField('Issue')
    
    def __unicode__(self):
        return self.title
    
    def __str__(self):
        return self.__unicode__()

    def get_absolute_url(self):
        return "/newspaper/{}/".format(self.id)
    
    def get_years(self):
        return self.issue_set.all()
    
    class Meta:
        ordering = ['title', ]
    

class Year(models.Model):
    year = models.IntegerField()
    # issues = models.ManyToManyField('Issue')
    
    def __unicode__(self):
        return self.year.__str__()
    
    def __str__(self):
        return self.__unicode__()
    
    class Meta:
        ordering = ['year', ]

    
class Issue(models.Model):
    newspaper = models.ForeignKey('Newspaper', null=True)
    year = models.ForeignKey('Year', null=True)
    date = models.DateField()
    issue = models.IntegerField(default=0)
    description = models.CharField(max_length=255, blank=True)
    
    def __unicode__(self):
        return "{} {}'{} {}".format(self.newspaper, self.issue, self.year, self.description)
        
    def __str__(self):
        return self.__unicode__()
    
    def url(self):
        return reverse('issue', args=[self.newspaper.slug, self.year, self.issue]) 
    
    def title_page(self):
        return self.article_set.get(page=1)   
    
    class Meta:
        ordering = ['newspaper', 'year', 'issue']