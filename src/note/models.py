from django.db import models
from django.core.urlresolvers import reverse


TEXT_NOTE = 1
LINKS_NOTE = 2
INTERVIEW_NOTE = 3

    
class NoteType(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=10000)
    
    def __unicode__(self):
        return self.title
        
    def __str__(self):
        return self.__unicode__()   
    
    def is_links(self):
        return self.pk == LINKS_NOTE 
    
    def is_interview(self):
        return self.pk == INTERVIEW_NOTE 


class Note(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    note_type = models.ForeignKey('NoteType', null=False)
    description = models.TextField(max_length=10000, null=True, blank=True)
    articles = models.ManyToManyField('article.Article', blank=True)
    
    def __unicode__(self):
        return "{}".format(self.title)
        
    def __str__(self):
        return self.__unicode__()
    
    def text(self):
        if self.note_type.is_interview():
            return "Interview\n{}".format(self.description)
        else:
            return self.description
    
    def url(self):
        return reverse('note', args=[self.slug])