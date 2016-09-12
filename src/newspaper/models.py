from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _


class Newspaper(models.Model):
    title = models.CharField(_('title'), max_length=255)
    description = models.TextField(_('description'), max_length=10000, blank=True)
    slug = models.SlugField(_('slug'), unique=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    def get_years(self):
        return self.issue_set.all()

    def url(self):
        return reverse('year', args=[self.slug])

    def prev(self):
        try:
            return Newspaper.objects.filter(id__lt=self.id).order_by('-id')[0]
        except (IndexError):
            return None

    def next(self):
        try:
            return Newspaper.objects.filter(id__gt=self.id).order_by('id')[0]
        except (IndexError):
            return None

    class Meta:
        verbose_name = _('newspaper')
        verbose_name_plural = _('newspapers')
        ordering = ['title', ]


class Year(models.Model):
    year = models.IntegerField(_('year'))

    def __unicode__(self):
        return self.year.__str__()

    def __str__(self):
        return self.__unicode__()

    def prev(self):
        try:
            print("LT")
            print(Year.objects.filter(year__lt=self.year).order_by('-year'))
            return Year.objects.filter(year__lt=self.year).order_by('-year')[0]
        except (IndexError):
            return None

    def next(self):
        try:
            print("GT")
            print(Year.objects.filter(year__gt=self.year).order_by('year'))
            return Year.objects.filter(year__gt=self.year).order_by('year')[0]
        except (IndexError):
            return None

    class Meta:
        verbose_name = _('year')
        verbose_name_plural = _('years')
        ordering = ['year', ]


class Issue(models.Model):
    newspaper = models.ForeignKey('Newspaper', verbose_name=_('newspaper'), null=True)
    year = models.ForeignKey('Year', verbose_name=_('year'), null=True)
    date = models.DateField(_('date'))
    issue = models.IntegerField(_('issue'), default=0)
    description = models.CharField(_('description'), max_length=255, blank=True)

    def __unicode__(self):
        return "{} {}'{}".format(self.newspaper, self.issue, self.year)

    def __str__(self):
        return self.__unicode__()

    def url(self):
        return reverse('issue', args=[self.newspaper.slug, self.year, self.issue])

    def title_page(self):
        return self.article_set.get(page=1)

    class Meta:
        verbose_name = _('issue')
        verbose_name_plural = _('issues')
        ordering = ['newspaper', 'year', 'issue']
