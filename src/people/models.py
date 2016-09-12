from django.db import models
from django.utils.translation import ugettext_lazy as _


class Person(models.Model):
    first_name = models.CharField(_('first name'), max_length=255, blank=True)
    last_name = models.CharField(_('last name'), max_length=255, blank=True)
    nickname = models.CharField(_('nickname'), max_length=255, blank=True)

    description = models.TextField(_('description'), max_length=10000, blank=True)
    slug = models.SlugField(_('slug'), unique=True)

    def __unicode__(self):
        titles = [self.first_name, ]
        if self.nickname:
            titles.append('"{}"'.format(self.nickname))
        titles.append(self.last_name)

        return " ".join(titles)

    def __str__(self):
        return self.__unicode__()

    def url(self):
        return "#"  # reverse('year', args=[self.slug])

    def prev(self):
        try:
            return Person.objects.filter(id__lt=self.id).order_by('-id')[0]
        except (IndexError):
            return None

    def next(self):
        try:
            return Person.objects.filter(id__gt=self.id).order_by('id')[0]
        except (IndexError):
            return None

    class Meta:
        verbose_name = _('person')
        verbose_name_plural = _('people')
        ordering = ['last_name', 'first_name', ]
