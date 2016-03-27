import datetime
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext as _
from taggit_autosuggest.managers import TaggableManager
from model_utils.models import TimeStampedModel


class ApprovedNewsManager(models.Manager):
    def get_queryset(self):
        return super(ApprovedNewsManager, self).get_queryset().filter(
            approved=True)


class NewsArticle(TimeStampedModel):

    """A PyAr news article."""

    title = models.CharField(max_length=255, verbose_name=_('Título'))
    introduction = models.TextField(null=True, blank=True,
                                    verbose_name=_('Introducción'))
    body = models.TextField(verbose_name=_('Contenido'))
    owner = models.ForeignKey(User)
    tags = TaggableManager(verbose_name=_('Etiquetas'), blank=True)
    approved = models.BooleanField(default=False)
    ts_moderate = models.DateTimeField(null=True, blank=True)
    user_moderate = models.TextField(null=True, blank=True)

    @models.permalink
    def get_absolute_url(self):
        return ('news_view', (self.id,), {})

    def moderate(self, approved, user_moderate):
        self.approved = approved
        self.user_moderate = user_moderate
        self.ts_moderate = datetime.datetime.now()
        self.save()

    def __unicode__(self):
        return u'{0}'.format(self.title)

    objects = models.Manager()
    approved_news = ApprovedNewsManager()

    class Meta:
        ordering = ('-created',)
