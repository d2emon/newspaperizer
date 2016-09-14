from django.db import models
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe


class World(models.Model):
    title = models.CharField(_('Title'), max_length=255, blank=False)
    slug = models.SlugField(_('Slug'), unique=True)
    image = models.ImageField(verbose_name=_('Image'), upload_to='images')
    description = models.TextField(_('Description'), max_length=10000, blank=True)

    def __unicode__(self):
        print(self.image.url)
        return self.title

    def __str__(self):
        return self.__unicode__()

    def get_absolute_url(self):
        return reverse('world', args=[self.slug])

    def preview(self):
        return mark_safe('<img src="{}" />'.format(self.image.url))

    preview.short_description = _('Image')

    def prev(self):
        try:
            return World.objects.filter(id__lt=self.id).order_by('-id')[0]
        except (IndexError):
            return None

    def next(self):
        try:
            return World.objects.filter(id__gt=self.id).order_by('id')[0]
        except (IndexError):
            return None

    class Meta:
        verbose_name = _('world')
        verbose_name_plural = _('worlds')
        ordering = ['title', ]
