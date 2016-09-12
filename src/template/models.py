from django.db import models
from django.utils.translation import ugettext_lazy as _


class ArticleTemplate(models.Model):
    newspaper = models.ForeignKey('newspaper.Newspaper', verbose_name=_('newspaper'), null=False)
    category = models.ForeignKey('article.ArticleCategory', verbose_name=_('category'), null=True)
    article_type = models.ForeignKey('article.ArticleType', verbose_name=_('type'), null=False)
    page = models.IntegerField(_('page'), default=1)

    def __unicode__(self):
        return "{} - {} ({})".format(self.newspaper, self.page, self.category.title)

    def __str__(self):
        return self.__unicode__()

    def text(self):
        return self.category.description

    class Meta:
        verbose_name = _('article template')
        verbose_name_plural = _('article templates')
        ordering = ['page', 'category__title']
