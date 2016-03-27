# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('jobs', '0011_job_approved'),
    ]

    operations = [
        migrations.AlterField(
            model_name='job',
            name='approved',
            field=models.BooleanField(default=False),
            preserve_default=True,
        ),
    ]
