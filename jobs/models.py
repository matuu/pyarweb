from autoslug import AutoSlugField
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse
from django.db import models
from django.utils.translation import ugettext as _
from taggit_autosuggest.managers import TaggableManager
from model_utils.models import TimeStampedModel

from pycompanies.models import Company
from community.models import ModerateModel


JOB_SENIORITIES = (
    ('Trainee', 'Trainee'),
    ('Junior', 'Junior'),
    ('Semi Senior', 'Semi Senior'),
    ('Senior', 'Senior'),
)


class ApprovedJobManager(models.Manager):
    def get_queryset(self):
        return super(ApprovedJobManager, self).get_queryset().filter(approved=True)


class Job(ModerateModel):
    """A PyAr Job."""

    title = models.CharField(max_length=255, verbose_name=_('Título'))
    company = models.ForeignKey(Company,
                                null=True,
                                blank=True,
                                verbose_name=_('Empresa'))
    description = models.TextField(verbose_name=_('Descripción'))
    location = models.CharField(max_length=100, verbose_name=_('Lugar'))
    email = models.EmailField()
    owner = models.ForeignKey(User)
    created = models.DateTimeField(auto_now_add=True)
    modified = models.DateTimeField(auto_now=True)
    tags = TaggableManager(verbose_name=_('Etiquetas'))
    remote_work = models.BooleanField(
        default=False,
        verbose_name=_('Trabajo Remoto'))
    seniority = models.CharField(
        max_length=100,
        blank=True,
        default='',
        choices=JOB_SENIORITIES,
        verbose_name=_('Experiencia'))
    slug = AutoSlugField(populate_from='title', unique=True)

    objects = models.Manager()
    approved_jobs = ApprovedJobManager()

    def __str__(self):
        return u'{0}'.format(self.title)

    @property
    def is_remote_work_allowed(self):
        return self.remote_work

    def get_absolute_url(self):
        return reverse('jobs_view', kwargs={'slug': self.slug})

    class Meta:
        ordering = ['-created']


class JobInactivated(TimeStampedModel):
    """ Jobs Inactivated """
    REASONS = (
        ('No es un trabajo relacionado con Python', 'No es un trabajo relacionado con Python'),
        ('Spam', 'Spam'),
        ('Información insuficiente', 'Información insuficiente'),
    )

    job = models.ForeignKey(Job)
    reason = models.CharField(
        max_length=100,
        blank=False,
        choices=REASONS,
        verbose_name=_('Motivo'))
    comment = models.TextField(blank=True,
                               null=True,
                               verbose_name=_('Comentario'))

    def __str__(self):
        return u'%s' % self.job.title

    def get_absolute_url(self):
        return reverse('jobs_list_all')

