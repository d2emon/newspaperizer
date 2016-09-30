from django.db import models
from django.urls import reverse
from django.utils.translation import ugettext_lazy as _
from django.utils.safestring import mark_safe
from newspaperizer.settings import settings
from django.core.files.storage import FileSystemStorage
from wiki.models import WikiPage

image_fs = FileSystemStorage(
    location=settings.get('worlds', dict()).get('images_root'),
    base_url=settings.get('worlds', dict()).get('images_url'),
)


class World(models.Model):
    title = models.CharField(_('Title'), max_length=255, blank=False)
    slug = models.SlugField(_('Slug'), unique=True)
    image = models.ImageField(verbose_name=_('Image'), storage=image_fs)  # upload_to=settings.get('worlds', dict()).get('images', 'images'))
    rating = models.PositiveIntegerField(_('Rating'), default=0)

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

    def get_attach_filename(self):
        import os
        return os.path.basename(self.image.name)

    def get_wiki(self):
        wiki_root = settings.get('worlds', dict()).get('wiki_root')
        attach_url = settings.get('worlds', dict()).get('attach_url')
        wiki_path = settings.get('worlds', dict()).get('wiki_path')

        w = WikiPage(root=wiki_root)
        w.root_url = reverse("path", kwargs={'path': wiki_path, })
        # "{}{}".format(reverse("wikiroot"), wiki_path)
        w.load(path="{}/".format(self.title))

        import logging
        logging.debug("Wiki Root: %s", wiki_root)
        return w
        # return load_wiki(wiki_root, self.title, attach="{}{}/__attach/".format(attach_url, self.title), href=reverse("wiki", kwargs={'path': "Миры/{}".format(self.title)}))

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
        ordering = ['-rating', 'title', ]
