# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


def active_to_approved(apps, schema_editor):
    """
    All actives jobs are marked as approved.
    """
    Job = apps.get_model("jobs", "Job")
    for job in Job.objects.all():
        job.approved = job.is_active
        job.save()

class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0012_auto_20160326_1940'),
    ]

    operations = [
        migrations.RunPython(active_to_approved)
    ]
