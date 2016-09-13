from django.db import models
from django.utils.translation import ugettext_lazy as _


SEX_UNKNOWN = 0
SEX_MALE = 1
SEX_FEMALE = 2


class HairColor(models.Model):
    color = models.CharField(_('color'), max_length=255)

    def __unicode__(self):
        return self.color

    def __str__(self):
        return self.__unicode__()


class Haircut(models.Model):
    title = models.CharField(_('title'), max_length=255)
    size = models.IntegerField(_('size'))

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()


class HairParting(models.Model):
    parting = models.CharField(_('parting'), max_length=255)

    def __unicode__(self):
        return self.parting

    def __str__(self):
        return self.__unicode__()


class EyeColor(models.Model):
    color = models.CharField(_('color'), max_length=255)

    def __unicode__(self):
        return self.color

    def __str__(self):
        return self.__unicode__()


class BreastSize(models.Model):
    size = models.CharField(_('size'), max_length=255)

    def __unicode__(self):
        return self.size

    def __str__(self):
        return self.__unicode__()


class Breast(models.Model):
    person = models.OneToOneField('Female')
    size = models.ForeignKey('BreastSize', verbose_name=_('breast size'), blank=True, null=True)
    areola = models.IntegerField(verbose_name=_('areola'), blank=True)


class Hair(models.Model):
    person = models.OneToOneField('Person', default=0)

    color = models.ForeignKey('HairColor', verbose_name=_('color'), blank=True, null=True)
    haircut = models.ForeignKey('Haircut', verbose_name=_('haircut'), blank=True, null=True)
    parting = models.ForeignKey('HairParting', verbose_name=_('parting'), blank=True, null=True)
    curling = models.BooleanField(_('curling'), blank=True)
    # models.ForeignKey('HairLength', verbose_name=_('length'), blank=True, null=True)


class Face(models.Model):
    person = models.OneToOneField('Person')

    eyebrow = models.CharField(_('eyebrow'), max_length=255, blank=True)
    eye = models.ForeignKey('EyeColor', verbose_name=_('eye'), blank=True, null=True)
    ear = models.CharField(_('ear'), max_length=255, blank=True)
    nose = models.CharField(_('nose'), max_length=255, blank=True)
    chick = models.CharField(_('chick'), max_length=255, blank=True)
    mouth = models.CharField(_('mouth'), max_length=255, blank=True)
    lip = models.CharField(_('lip'), max_length=255, blank=True)
    chin = models.CharField(_('chin'), max_length=255, blank=True)
    neck = models.CharField(_('neck'), max_length=255, blank=True)


class Cloth(models.Model):
    person = models.OneToOneField('Person')

    head = models.CharField(_('head'), max_length=255, blank=True)
    body = models.CharField(_('body'), max_length=255, blank=True)
    belt = models.CharField(_('belt'), max_length=255, blank=True)
    legs = models.CharField(_('legs'), max_length=255, blank=True)
    feet = models.CharField(_('feet'), max_length=255, blank=True)


class Person(models.Model):
    first_name = models.CharField(_('first name'), max_length=255, blank=True)
    last_name = models.CharField(_('last name'), max_length=255, blank=True)
    nickname = models.CharField(_('nickname'), max_length=255, blank=True)
    slug = models.SlugField(_('slug'), unique=True)
    sex = SEX_UNKNOWN

    body = models.CharField(_('body'), max_length=255, blank=True)
    arm = models.CharField(_('arm'), max_length=255, blank=True)
    hand = models.CharField(_('hand'), max_length=255, blank=True)
    leg = models.CharField(_('leg'), max_length=255, blank=True)
    foot = models.CharField(_('foot'), max_length=255, blank=True)

    description = models.TextField(_('description'), max_length=10000, blank=True)

    def __unicode__(self):
        titles = [self.first_name, ]
        if self.nickname:
            titles.append('"{}"'.format(self.nickname))
        titles.append(self.last_name)

        return " ".join(titles)

    def __str__(self):
        return self.__unicode__()

    def hair(self):
        return self.face.hair

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


class Male(Person):
    sex = SEX_MALE


class Female(Person):
    sex = SEX_FEMALE


# class Conchita(Person):
#    sex = models.IntegerField(_('sex'), choices=(
#        (SEX_UNKNOWN, _('Unknown')),
#        (SEX_MALE, _('Male')),
#        (SEX_FEMALE, _('Female')),
#    ), default=SEX_UNKNOWN)
