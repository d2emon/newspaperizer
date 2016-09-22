from django.db import models
# from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from newspaperizer.settings import settings
from django.core.files.storage import FileSystemStorage
from people.models import Person


image_fs = FileSystemStorage(
    location=settings.get('books', dict()).get('images_root'),
    base_url=settings.get('books', dict()).get('images_url'),
)


genre_image_fs = FileSystemStorage(
    location=settings.get('books', dict()).get('genres', dict()).get('images_root'),
    base_url=settings.get('books', dict()).get('genres', dict()).get('images_url'),
)


class BookGenre(models.Model):
    parent = models.ManyToManyField('self', verbose_name=_('Parent genre'), blank=True, )
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), unique=True)
    folder = models.CharField(_('Folder'), max_length=255, blank=True)
    image = models.ImageField(verbose_name=_('Image'), storage=genre_image_fs, blank=True)
    description = models.TextField(_('Description'), max_length=10000, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    # def get_absolute_url(self):
    #     return reverse('book_genre', args=[self.slug])

    class Meta:
        verbose_name = _('Book genre')
        verbose_name_plural = _('Book genres')
        ordering = ['title', ]


class Book(models.Model):
    authors = models.ManyToManyField(Person, verbose_name=_('Authors'), blank=True)
    genre = models.ManyToManyField('BookGenre', verbose_name=_('Genres'))
    title = models.CharField(_('Title'), max_length=255)
    slug = models.SlugField(_('Slug'), unique=True)
    folder = models.CharField(_('Folder'), max_length=255)
    image = models.ImageField(verbose_name=_('Image'), storage=image_fs, blank=True)
    description = models.TextField(_('Description'), max_length=10000, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    # def get_absolute_url(self):
    #     return reverse('book_genre', args=[self.slug])

    class Meta:
        verbose_name = _('Book')
        verbose_name_plural = _('Books')
        ordering = ['title', ]
