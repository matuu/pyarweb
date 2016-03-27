from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from taggit_autosuggest.managers import TaggableManager
from model_utils.models import TimeStampedModel
from community.models import ModerateModel


class ApprovedNewsManager(models.Manager):
    def get_queryset(self):
        return super(ApprovedNewsManager, self).get_queryset().filter(
            approved=True)


class NewsArticle(TimeStampedModel, ModerateModel):

    """A PyAr news article."""

    title = models.CharField(max_length=255, verbose_name=_('Título'))
    introduction = models.TextField(null=True, blank=True,
                                    verbose_name=_('Introducción'))
    body = models.TextField(verbose_name=_('Contenido'))
    owner = models.ForeignKey(User)
    tags = TaggableManager(verbose_name=_('Etiquetas'), blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('news_view', (self.id,), {})

    def __unicode__(self):
        return u'{0}'.format(self.title)

    objects = models.Manager()
    approved_news = ApprovedNewsManager()

    class Meta:
        ordering = ('-created',)
