from django.db import models
from django.core.urlresolvers import reverse


TEXT_ARTICLE = 1
LINKS_ARTICLE = 2
NOTES_ARTICLE = 3
INTERVIEW_ARTICLE = 4


class ArticleCategory(models.Model):
    title = models.CharField(max_length=255)
    newspaper = models.ForeignKey('newspaper.Newspaper', null=True)
    description = models.TextField(max_length=10000)
    
    def __unicode__(self):
        return "{} ({})".format(self.title, self.newspaper)
        
    def __str__(self):
        return self.__unicode__()    
   
    
class ArticleType(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    
    def __unicode__(self):
        return self.title
        
    def __str__(self):
        return self.__unicode__()   
    
    def is_links(self):
        return self.pk == LINKS_ARTICLE 
    
    def is_notes(self):
        return self.pk == NOTES_ARTICLE 
   
    
class Article(models.Model):
    title = models.CharField(max_length=255, null=True, blank=True)
    issue = models.ForeignKey('newspaper.Issue', null=True)
    category = models.ForeignKey('ArticleCategory', null=True)
    article_type = models.ForeignKey('ArticleType', null=False)
    linked = models.ManyToManyField('Article', blank=True)
    page = models.IntegerField(default=1)
    description = models.TextField(max_length=10000, null=True, blank=True)
    
    def __unicode__(self):
        return "{} ({}, {} - {})".format(self.title, self.issue, self.page, self.category.title)
        
    def __str__(self):
        return self.__unicode__()
    
    def text(self):
        if self.article_type.is_notes():
            return "NOTES\n{}".format(self.description)
        else:
            return self.description
        
    def unempty_title(self):
        if self.title:
            return self.title
        return self.category.title
    
    def url(self):
        return reverse('article', args=[self.issue.newspaper.slug, self.issue.year, self.issue.issue, self.page])
    
    class Meta:
        ordering = ['issue', 'page', 'title']        