# from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from book.models import ScienceBook


class BookGames(ScienceBook):
    authors = None
    genre = None
    # title = models.CharField(_('Title'), max_length=255)
    # slug = models.SlugField(_('Slug'), unique=True)
    folder = None
    # image = models.ImageField(verbose_name=_('Image'), storage=image_fs, blank=True)
    # description = models.TextField(_('Description'), max_length=10000, blank=True)

    def get_absolute_url(self):
        return reverse('book', args=[self.slug])

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
        ordering = ['title', ]
