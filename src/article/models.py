from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


TEXT_ARTICLE = 1
LINKS_ARTICLE = 2
NOTES_ARTICLE = 3
INTERVIEW_ARTICLE = 4


class ArticleCategory(models.Model):
    title = models.CharField(_('title'), max_length=255)
    newspaper = models.ForeignKey('newspaper.Newspaper', verbose_name=_('newspaper'), null=True)
    description = models.TextField(_('description'), max_length=10000)

    def __unicode__(self):
        return "{} ({})".format(self.title, self.newspaper)

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _('category')
        verbose_name_plural = _('categories')
        ordering = ['title']


class ArticleType(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), max_length=10000)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    def is_links(self):
        return self.pk == LINKS_ARTICLE

    def is_notes(self):
        return self.pk == NOTES_ARTICLE

    class Meta:
        verbose_name = _('article type')
        verbose_name_plural = _('article_types')


class Article(models.Model):
    title = models.CharField(_('title'), max_length=255, null=True, blank=True)
    issue = models.ForeignKey('newspaper.Issue', verbose_name=_('issue'), null=True)
    category = models.ForeignKey('ArticleCategory', verbose_name=_('category'), null=True)
    article_type = models.ForeignKey('ArticleType', verbose_name=_('type'), null=False)
    linked = models.ManyToManyField('self', verbose_name=_('linked articles'), blank=True)
    page = models.IntegerField(_('page'), default=1)
    description = models.TextField(_('description'), max_length=10000, null=True, blank=True)

    def __unicode__(self):
        return "{} ({}, {} - {})".format(self.title, self.issue, self.page, self.category.title)

    def __str__(self):
        return self.__unicode__()

    def text(self):
        # if self.article_type.is_notes():
            # return "NOTES\n{}".format(self.description)

        return self.description

    def notes_title(self):
        if self.article_type.is_notes():
            return ''
        elif self.note_set.count() >= 1:
            return self.note_set.all()[0].title
        else:
            return ''

    def unempty_title(self):
        if self.title:
            return self.title
        elif self.notes_title():
            return self.notes_title()
        return self.category.title

    def url(self):
        return reverse('article', args=[self.issue.newspaper.slug, self.issue.year, self.issue.issue, self.page])

    def prev(self):
        page = self.issue.article_set.filter(page__lt=self.page).order_by('-page')
        if page.count():
            return page[0]
        else:
            return False

    def next(self):
        page = self.issue.article_set.filter(page__gt=self.page).order_by('page')
        if page.count():
            return page[0]
        else:
            return False

    class Meta:
        verbose_name = _('article')
        verbose_name_plural = _('articles')
        ordering = ['issue', 'page', 'title']
