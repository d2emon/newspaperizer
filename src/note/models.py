from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


TEXT_NOTE = 1
LINKS_NOTE = 2
INTERVIEW_NOTE = 3


class NoteType(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), max_length=10000)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    def is_links(self):
        return self.pk == LINKS_NOTE

    def is_interview(self):
        return self.pk == INTERVIEW_NOTE

    class Meta:
        verbose_name = _('note type')
        verbose_name_plural = _('note types')


class Note(models.Model):
    title = models.CharField(_('title'), max_length=255)
    slug = models.SlugField(_('slug'), unique=True)
    note_type = models.ForeignKey('NoteType', verbose_name=_('note type'), null=False)
    description = models.TextField(_('description'), max_length=10000, null=True, blank=True)
    articles = models.ManyToManyField('article.Article', verbose_name=_('articles'), blank=True)

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

    class Meta:
        verbose_name = _('note')
        verbose_name_plural = _('notes')
