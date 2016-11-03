from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _


class News(models.Model):
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), unique=True)    
    date = models.DateField(_('date'))
    brief = models.TextField(_('brief'), max_length=512)
    description = models.TextField(_('description'), max_length=10000)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    def get_absolute_url(self):
        return reverse('news_article', kwargs={"slug": self.slug, })

    class Meta:
        verbose_name = _('news')
        verbose_name_plural = _('news')
        ordering = ['date', ]