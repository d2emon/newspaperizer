from django.db import models
from django.utils.translation import ugettext_lazy as _


GAME_UNKNOWN = 0
GAME_VIDEO = 1
GAME_BOARD = 2
GAME_RPG = 3
GAME_MINI = 4
GAME_BOOK = 5
GAME_MIND = 6
GAME_OUTDOOR = 7
GAME_SPORT = 8


class VideoGameGenre(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=False)
    slug = models.SlugField(_('slug'), unique=True)
    description = models.TextField(_('description'), max_length=10000, blank=True)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _('video game genre')
        verbose_name_plural = _('video game genres')
        ordering = ['title', ]    

class Game(models.Model):
    title = models.CharField(_('title'), max_length=255, blank=False)
    slug = models.SlugField(_('slug'), unique=True)
    description = models.TextField(_('description'), max_length=10000, blank=True)
    game_type = GAME_UNKNOWN

    def __unicode__(self):
        return self.title

    def __str__(self):
        return self.__unicode__()

    class Meta:
        verbose_name = _('game')
        verbose_name_plural = _('games')
        ordering = ['title', ]    
    

class OutdoorGame(Game):
    game_type = GAME_OUTDOOR

    class Meta:
        verbose_name = _('outdoor game')
        verbose_name_plural = _('outdoor games')
            

class GameBook(Game):
    game_type = GAME_BOOK

    class Meta:
        verbose_name = _('gamebook')
        verbose_name_plural = _('gamebooks')
    

class VideoGame(Game):
    game_type = GAME_VIDEO
    genre = models.ForeignKey('VideoGameGenre', verbose_name=_('genre'), blank=False, null=False)

    class Meta:
        verbose_name = _('video game')
        verbose_name_plural = _('video games')
    

class BoardGame(Game):
    game_type = GAME_BOARD        

    class Meta:
        verbose_name = _('board game')
        verbose_name_plural = _('board games')
    

class RoleplayGame(Game):
    game_type = GAME_RPG

    class Meta:
        verbose_name = _('RPG')
        verbose_name_plural = _('RPGs')    